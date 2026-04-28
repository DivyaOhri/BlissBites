# -*- coding: utf-8 -*-
"""
Data Storage Module for MoodBite
Handles persistent storage for user profiles and mood/food history
Now with Vector Database integration for semantic search
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

# Data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
PROFILE_FILE = os.path.join(DATA_DIR, "profiles.json")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.json")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Import vector store (lazy loading to avoid startup issues)
_vector_store = None

def _get_vector_store():
    """Lazy load vector store to avoid import errors."""
    global _vector_store
    if _vector_store is None:
        try:
            from vector_store import (
                add_profile_vector, find_similar_profiles,
                add_feedback_vector, find_similar_feedback,
                get_popular_foods, add_mood_entry, get_mood_trends,
                hybrid_food_search, initialize_all_collections
            )
            _vector_store = {
                "add_profile": add_profile_vector,
                "find_similar_profiles": find_similar_profiles,
                "add_feedback": add_feedback_vector,
                "find_similar_feedback": find_similar_feedback,
                "get_popular_foods": get_popular_foods,
                "add_mood_entry": add_mood_entry,
                "get_mood_trends": get_mood_trends,
                "hybrid_search": hybrid_food_search,
                "init": initialize_all_collections
            }
        except ImportError as e:
            print(f"Vector store not available: {e}")
            return None
    return _vector_store


def _load_json(file_path: str, default: Any = None) -> Any:
    """Load JSON from file, return default if file doesn't exist or is empty or invalid."""
    if default is None:
        default = []
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Handle empty dict case for list-expected files
                if isinstance(data, dict) and not data and default == []:
                    return []
                return data
    except (json.JSONDecodeError, IOError):
        pass
    return default


def _save_json(file_path: str, data: Any) -> None:
    """Save data to JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ==================== PROFILE MANAGEMENT ====================

def save_profile(user_id: str, profile_data: Dict) -> Dict:
    """
    Save or update user profile.
    Also stores in vector database for semantic similarity search.
    
    Args:
        user_id: Unique identifier for the user
        profile_data: Dict with keys like name, dietary, cuisine, budget
    
    Returns:
        Dict with success status and message
    """
    profiles = _load_json(PROFILE_FILE, {})
    
    # Update profile with timestamp
    profile_data["updated_at"] = datetime.now().isoformat()
    profiles[user_id] = profile_data
    
    _save_json(PROFILE_FILE, profiles)
    
    # Also store in vector database for semantic search
    vs = _get_vector_store()
    if vs:
        vs["add_profile"](user_id, profile_data)
    
    return {"success": True, "message": "Profile saved successfully"}


def get_profile(user_id: str) -> Optional[Dict]:
    """Get user profile by user_id."""
    profiles = _load_json(PROFILE_FILE, {})
    return profiles.get(user_id)


def get_all_profiles() -> Dict:
    """Get all profiles."""
    return _load_json(PROFILE_FILE, {})


# ==================== FEEDBACK MANAGEMENT ====================

def save_feedback(feedback_data: Dict) -> Dict:
    """
    Saves dual-layered feedback (App Experience + Specific Food).
    Standardizes ratings as integers for future calculations.
    """
    feedback_list = _load_json(FEEDBACK_FILE, [])
    
    # 1. ADD SYSTEM METADATA
    feedback_data["timestamp"] = datetime.now().isoformat()
    feedback_data["id"] = len(feedback_list) + 1
    
    # 2. DATA CLEANING: Convert string ratings from JS to Integers
    # 'app_rating' = Site feedback | 'rating' = Food item feedback
    if feedback_data.get("app_rating"):
        try:
            feedback_data["app_rating"] = int(feedback_data["app_rating"])
        except ValueError:
            pass

    if feedback_data.get("rating"):
        try:
            feedback_data["rating"] = int(feedback_data["rating"])
        except ValueError:
            pass

    # 3. PERSIST TO JSON
    feedback_list.append(feedback_data)
    _save_json(FEEDBACK_FILE, feedback_list)
    
    # 4. VECTOR DATABASE INTEGRATION (Optional Sentiment Search)
    vs = _get_vector_store()
    if vs:
        try:
            # We index the suggestions/comments for semantic search later
            vs["add_feedback"](str(feedback_data["id"]), feedback_data)
        except Exception as e:
            print(f"Vector Store indexing skipped: {e}")
    
    return {
        "success": True, 
        "message": "Feedback saved successfully", 
        "feedback_id": feedback_data["id"]
    }

def get_feedback(user_id: Optional[str] = None) -> List[Dict]:
    """Get all feedback, optionally filtered by user_id."""
    feedback_list = _load_json(FEEDBACK_FILE, [])
    
    if user_id:
        return [f for f in feedback_list if f.get("user_id") == user_id]
    return feedback_list


# ==================== HISTORY MANAGEMENT ====================

def save_history(user_id: str, history_data: Dict) -> Dict:
    """
    Save mood check and food recommendation history.
    Also stores mood entries in vector database for trend analysis.
    
    Args:
        user_id: Unique identifier for the user
        history_data: Dict with mood, energy, stress, foods recommended, etc.
    
    Returns:
        Dict with success status and message
    """
    history = _load_json(HISTORY_FILE, {})
    
    if user_id not in history:
        history[user_id] = []
    
    # Add timestamp
    history_data["timestamp"] = datetime.now().isoformat()
    history_data["id"] = len(history[user_id]) + 1
    
    history[user_id].append(history_data)
    _save_json(HISTORY_FILE, history)
    
    # Also store mood entry in vector database for trend analysis
    vs = _get_vector_store()
    if vs:
        foods = history_data.get("foods", [])
        if isinstance(foods, str):
            foods = [foods]
        vs["add_mood_entry"](
            user_id,
            history_data.get("mood", ""),
            history_data.get("energy", ""),
            foods
        )
    
    return {"success": True, "message": "History saved", "history_id": history_data["id"]}


def get_history(user_id: str, limit: int = 10) -> List[Dict]:
    """Get user's mood/food history, most recent first."""
    history = _load_json(HISTORY_FILE, {})
    user_history = history.get(user_id, [])
    
    # Return most recent first, limited to 'limit' items
    return list(reversed(user_history))[:limit]


def get_all_history() -> Dict:
    """Get all history for all users."""
    return _load_json(HISTORY_FILE, {})


# ==================== STATS ====================

def get_user_stats(user_id: str) -> Dict:
    """Get statistics for a user."""
    history = get_history(user_id)
    feedback = get_feedback(user_id)
    profile = get_profile(user_id)
    
    # Calculate stats
    mood_counts = {}
    food_counts = {}
    total_spend = 0
    
    for h in history:
        mood = h.get("mood", "unknown")
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
        
        for food in h.get("foods", []):
            food_name = food.get("name", "unknown")
            food_counts[food_name] = food_counts.get(food_name, 0) + 1
            total_spend += food.get("price", 0)
    
    avg_rating = 0
    if feedback:
        ratings = [f.get("rating", 0) for f in feedback if f.get("rating")]
        if ratings:
            avg_rating = sum(ratings) / len(ratings)
    
    return {
        "total_mood_checks": len(history),
        "total_feedback": len(feedback),
        "mood_counts": mood_counts,
        "top_foods": sorted(food_counts.items(), key=lambda x: x[1], reverse=True)[:5],
        "total_spent": total_spend,
        "average_rating": round(avg_rating, 1) if avg_rating else 0,
        "profile": profile
    }


def get_food_ratings_summary() -> Dict[str, Dict]:
    """Scans feedback.json and calculates average rating + count for every food."""
    all_feedback = _load_json(FEEDBACK_FILE, [])
    summary = {}

    for entry in all_feedback:
        food_name = entry.get("food_name")
        rating = entry.get("rating")

        if food_name and rating:
            if food_name not in summary:
                summary[food_name] = {"total": 0, "count": 0}
            summary[food_name]["total"] += int(rating)
            summary[food_name]["count"] += 1

    # Convert totals into averages
    return {
        name: {
            "avg": round(stats["total"] / stats["count"], 1),
            "count": stats["count"]
        } for name, stats in summary.items()
    }