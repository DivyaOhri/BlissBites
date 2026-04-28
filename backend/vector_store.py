# -*- coding: utf-8 -*-
"""
Vector Store Module for BlissBites
Manages all vector database operations using ChromaDB
with multiple collections for foods, profiles, and feedback.
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

# Import FOOD_DATA directly from food_data to avoid circular import
from food_data import FOOD_DATA

# Initialize embedding model and ChromaDB client
_model = None
_client = None

# Data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
PROFILE_FILE = os.path.join(DATA_DIR, "profiles.json")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.json")


def _get_model():
    """Get or initialize the sentence transformer model."""
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _get_client():
    """Get or initialize the ChromaDB client."""
    global _client
    if _client is None:
        # Use persistent client to store data locally
        persist_dir = os.path.join(os.path.dirname(__file__), "chroma_data")
        os.makedirs(persist_dir, exist_ok=True)
        _client = chromadb.PersistentClient(path=persist_dir)
    return _client


def _load_json(file_path: str, default: Any = None) -> Any:
    """Load JSON from file, return default if file doesn't exist or is empty."""
    if default is None:
        default = []
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError):
        pass
    return default


def _save_json(file_path: str, data: Any) -> None:
    """Save data to JSON file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ==================== FOOD COLLECTION ====================

def init_food_collection():
    """Initialize the food collection with embeddings."""
    client = _get_client()
    collection = client.get_or_create_collection("foods")
    
    if collection.count() == 0:
        model = _get_model()
        for i, food in enumerate(FOOD_DATA):
            tag_text = " ".join(food["tags"])
            embedding = model.encode(tag_text).tolist()
            collection.add(
                ids=[str(i)],
                embeddings=[embedding],
                documents=[tag_text],
                metadatas=[{
                    "name": food["name"],
                    "price": food["price"],
                    "restaurant": food["restaurant"],
                    "tags": ",".join(food["tags"])
                }]
            )
    return collection


def search_foods(keywords: list, top_k: int = 3, max_price: int = 1000) -> list:
    """Search foods using vector similarity with price filtering."""
    try:
        model = _get_model()
        collection = init_food_collection()
        
        query_text = " ".join(keywords)
        query_embedding = model.encode(query_text).tolist()
        
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=min(10, len(FOOD_DATA))
        )
        
        foods = []
        for i, metadata in enumerate(results["metadatas"][0]):
            if metadata["price"] <= max_price:
                foods.append({
                    "name": metadata["name"],
                    "price": metadata["price"],
                    "restaurant": metadata["restaurant"],
                    "tags": metadata["tags"].split(","),
                    "score": round(1 - results["distances"][0][i], 3)
                })
        
        return foods[:top_k]
    
    except Exception as e:
        print(f"Vector search error (foods): {e}")
        return _fallback_food_search(keywords, top_k)


def _fallback_food_search(keywords: list, top_k: int = 3) -> list:
    """Simple keyword-match fallback."""
    keywords_lower = [k.lower() for k in keywords]
    results = []
    
    for food in FOOD_DATA:
        if any(kw in " ".join(food["tags"]).lower() for kw in keywords_lower):
            results.append({
                "name": food["name"],
                "price": food["price"],
                "restaurant": food["restaurant"],
                "tags": food["tags"],
                "score": 0.5
            })
    
    return results[:top_k]


# ==================== PROFILE COLLECTION ====================

def init_profile_collection():
    """Initialize the profile collection."""
    client = _get_client()
    return client.get_or_create_collection("profiles")


def add_profile_vector(user_id: str, profile_data: Dict) -> bool:
    """Add or update a user profile in the vector store."""
    try:
        collection = init_profile_collection()
        model = _get_model()
        
        # Create searchable text from profile
        search_text = _create_profile_search_text(profile_data)
        embedding = model.encode(search_text).tolist()
        
        collection.upsert(
            ids=[user_id],
            embeddings=[embedding],
            documents=[search_text],
            metadatas=[{
                "name": profile_data.get("name", ""),
                "dietary": profile_data.get("dietary", ""),
                "cuisine": profile_data.get("cuisine", ""),
                "budget": profile_data.get("budget", 100),
                "updated_at": datetime.now().isoformat()
            }]
        )
        return True
    except Exception as e:
        print(f"Error adding profile to vector store: {e}")
        return False


def _create_profile_search_text(profile: Dict) -> str:
    """Create searchable text from profile data."""
    parts = []
    if profile.get("name"):
        parts.append(f"user {profile['name']}")
    if profile.get("dietary"):
        parts.append(f"dietary {profile['dietary']}")
    if profile.get("cuisine"):
        parts.append(f"prefers {profile['cuisine']} cuisine")
    if profile.get("budget"):
        parts.append(f"budget {profile['budget']}")
    return " ".join(parts) if parts else "general user"


def find_similar_profiles(user_id: str, top_k: int = 3) -> list:
    """Find profiles similar to a given user."""
    try:
        collection = init_profile_collection()
        
        # Get the user's profile embedding
        result = collection.get(ids=[user_id])
        
        if not result["embeddings"]:
            return []
        
        user_embedding = result["embeddings"][0]
        
        # Search for similar profiles (excluding self)
        results = collection.query(
            query_embeddings=[user_embedding],
            n_results=top_k + 1
        )
        
        similar = []
        for i, pid in enumerate(results["ids"][0]):
            if pid != user_id:
                similar.append({
                    "user_id": pid,
                    "name": results["metadatas"][0][i].get("name", ""),
                    "score": round(1 - results["distances"][0][i], 3)
                })
        
        return similar[:top_k]
    
    except Exception as e:
        print(f"Error finding similar profiles: {e}")
        return []


# ==================== FEEDBACK COLLECTION ====================

def init_feedback_collection():
    """Initialize the feedback collection."""
    client = _get_client()
    return client.get_or_create_collection("feedback")


def add_feedback_vector(feedback_id: str, feedback_data: Dict) -> bool:
    """Add feedback to the vector store for analysis."""
    try:
        collection = init_feedback_collection()
        model = _get_model()
        
        # Create searchable text from feedback
        search_text = _create_feedback_search_text(feedback_data)
        embedding = model.encode(search_text).tolist()
        
        collection.upsert(
            ids=[str(feedback_id)],
            embeddings=[embedding],
            documents=[search_text],
            metadatas=[{
                "user_id": feedback_data.get("user_id", ""),
                "food_name": feedback_data.get("food_name", ""),
                "rating": feedback_data.get("rating", 0),
                "mood": feedback_data.get("mood", ""),
                "timestamp": feedback_data.get("timestamp", "")
            }]
        )
        return True
    except Exception as e:
        print(f"Error adding feedback to vector store: {e}")
        return False


def _create_feedback_search_text(feedback: Dict) -> str:
    """Create searchable text from feedback data."""
    parts = []
    if feedback.get("food_name"):
        parts.append(f"food {feedback['food_name']}")
    if feedback.get("comment"):
        parts.append(feedback["comment"])
    if feedback.get("mood"):
        parts.append(f"mood {feedback['mood']}")
    if feedback.get("rating"):
        parts.append(f"rating {feedback['rating']}")
    return " ".join(parts) if parts else "general feedback"


def find_similar_feedback(food_name: str = None, mood: str = None, top_k: int = 5) -> list:
    """Find similar feedback based on food name or mood."""
    try:
        collection = init_feedback_collection()
        model = _get_model()
        
        # Build query text
        query_parts = []
        if food_name:
            query_parts.append(f"food {food_name}")
        if mood:
            query_parts.append(f"mood {mood}")
        
        if not query_parts:
            return []
        
        query_text = " ".join(query_parts)
        query_embedding = model.encode(query_text).tolist()
        
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        feedback_list = []
        for i, fid in enumerate(results["ids"][0]):
            meta = results["metadatas"][0][i]
            feedback_list.append({
                "id": fid,
                "user_id": meta.get("user_id", ""),
                "food_name": meta.get("food_name", ""),
                "rating": meta.get("rating", 0),
                "mood": meta.get("mood", ""),
                "score": round(1 - results["distances"][0][i], 3)
            })
        
        return feedback_list
    
    except Exception as e:
        print(f"Error finding similar feedback: {e}")
        return []


def get_popular_foods(min_rating: float = 3.0, top_k: int = 5) -> list:
    """Get popular foods based on feedback ratings."""
    try:
        collection = init_feedback_collection()
        
        # Get all feedback
        results = collection.get()
        
        if not results["ids"]:
            return []
        
        # Aggregate ratings by food
        food_ratings = {}
        for i, meta in enumerate(results["metadatas"]):
            food = meta.get("food_name", "")
            rating = meta.get("rating", 0)
            
            if food and rating >= min_rating:
                if food not in food_ratings:
                    food_ratings[food] = []
                food_ratings[food].append(rating)
        
        # Calculate average ratings
        popular = []
        for food, ratings in food_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            popular.append({
                "food_name": food,
                "avg_rating": round(avg_rating, 2),
                "count": len(ratings)
            })
        
        # Sort by average rating
        popular.sort(key=lambda x: x["avg_rating"], reverse=True)
        return popular[:top_k]
    
    except Exception as e:
        print(f"Error getting popular foods: {e}")
        return []


# ==================== MOOD HISTORY COLLECTION ====================

def init_mood_history_collection():
    """Initialize the mood history collection."""
    client = _get_client()
    return client.get_or_create_collection("mood_history")


def add_mood_entry(user_id: str, mood: str, energy: str, foods_recommended: List[str]) -> bool:
    """Add a mood entry to history for trend analysis."""
    try:
        collection = init_mood_history_collection()
        model = _get_model()
        
        entry_id = f"{user_id}_{datetime.now().timestamp()}"
        
        search_text = f"mood {mood} energy {energy} foods {', '.join(foods_recommended)}"
        embedding = model.encode(search_text).tolist()
        
        collection.add(
            ids=[entry_id],
            embeddings=[embedding],
            documents=[search_text],
            metadatas=[{
                "user_id": user_id,
                "mood": mood,
                "energy": energy,
                "foods": ",".join(foods_recommended),
                "timestamp": datetime.now().isoformat()
            }]
        )
        return True
    except Exception as e:
        print(f"Error adding mood entry: {e}")
        return False


def get_mood_trends(user_id: str, top_k: int = 10) -> list:
    """Get recent mood history for a user."""
    try:
        collection = init_mood_history_collection()
        
        # Get all entries for this user
        results = collection.get()
        
        if not results["ids"]:
            return []
        
        user_entries = []
        for i, meta in enumerate(results["metadatas"]):
            if meta.get("user_id") == user_id:
                user_entries.append({
                    "mood": meta.get("mood", ""),
                    "energy": meta.get("energy", ""),
                    "foods": meta.get("foods", "").split(","),
                    "timestamp": meta.get("timestamp", ""),
                    "score": round(1 - results["distances"][0][i], 3) if results.get("distances") else 0
                })
        
        # Sort by timestamp and return recent
        user_entries.sort(key=lambda x: x["timestamp"], reverse=True)
        return user_entries[:top_k]
    
    except Exception as e:
        print(f"Error getting mood trends: {e}")
        return []


# ==================== HYBRID SEARCH ====================

def hybrid_food_search(
    keywords: list,
    user_preferences: Dict = None,
    max_price: int = 1000,
    top_k: int = 3
) -> list:
    """
    Advanced food search combining vector similarity with user preferences.
    
    Args:
        keywords: Search keywords from mood analysis
        user_preferences: User profile data (dietary restrictions, cuisine, budget)
        max_price: Maximum price filter
        top_k: Number of results to return
    
    Returns:
        List of recommended foods with scores
    """
    try:
        # Step 1: Vector search with keywords
        vector_results = search_foods(keywords, top_k=top_k * 2, max_price=max_price)
        
        if not user_preferences:
            return vector_results[:top_k]
        
        # Step 2: Re-rank based on user preferences
        reranked = []
        for food in vector_results:
            score = food["score"]
            
            # Boost score for matching dietary preferences
            dietary = user_preferences.get("dietary", "").lower()
            if dietary and dietary in " ".join(food.get("tags", [])).lower():
                score += 0.2
            
            # Boost score for preferred cuisine
            cuisine = user_preferences.get("cuisine", "").lower()
            if cuisine and cuisine in food.get("restaurant", "").lower():
                score += 0.15
            
            # Adjust for budget
            if food["price"] <= user_preferences.get("budget", 1000):
                score += 0.1
            
            reranked.append({**food, "final_score": round(score, 3)})
        
        # Sort by final score
        reranked.sort(key=lambda x: x["final_score"], reverse=True)
        return reranked[:top_k]
    
    except Exception as e:
        print(f"Error in hybrid search: {e}")
        return search_foods(keywords, top_k, max_price)


# ==================== INITIALIZATION ====================

def initialize_all_collections():
    """Initialize all vector collections. Call on app startup."""
    init_food_collection()
    init_profile_collection()
    init_feedback_collection()
    init_mood_history_collection()
    print("✓ All vector collections initialized")


# For backward compatibility
def get_food_collection():
    return init_food_collection()


def get_all_collections():
    """Get all collection names."""
    client = _get_client()
    return [col.name for col in client.list_collections()]