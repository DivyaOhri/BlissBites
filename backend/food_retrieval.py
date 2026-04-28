"""
Vector DB + Food Retrieval
Smart Food Recommender — Emotion-Aware Analysis
CSU2217 | Yogananda School of AI, Shoolini University

Real menu data from restaurants near Shoolini University, Solan.
Uses ChromaDB for local vector storage + sentence-transformers for embeddings.

Now with enhanced hybrid search using the centralized vector_store module.
"""


import os
import re
import chromadb
from sentence_transformers import SentenceTransformer
from food_data import FOOD_DATA
from data_storage import get_food_ratings_summary

# 1. Global variables to keep the model in memory
_model = None
_collection = None
_client = None

def _get_model():
    global _model
    if _model is None:
        # Loading the model takes time; we do it once
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def _get_collection():
    global _collection, _client
    if _collection is None:
        # CHANGE: Use PersistentClient so embeddings are saved to your disk
        db_path = os.path.join(os.path.dirname(__file__), "moodbite_db")
        _client = chromadb.PersistentClient(path=db_path)
        _collection = _client.get_or_create_collection("moodbite_foods")

        if _collection.count() == 0:
            print("🚀 First-time setup: Indexing 1527 items. This will take a minute...")
            model = _get_model()
            ids, embeddings, documents, metadatas = [], [], [], []
            
            for i, food in enumerate(FOOD_DATA):
                # Weighting: Name is repeated to ensure it's "louder" than tags
                searchable_text = f"ITEM: {food['name']} {food['name']}. VIBE: {', '.join(food['tags'])}"
                embedding = model.encode(searchable_text).tolist()
                
                ids.append(str(i))
                embeddings.append(embedding)
                documents.append(searchable_text)
                
                # CRITICAL FIX: ChromaDB metadata cannot store lists. 
                # We convert tags to a comma-separated string.
                metadatas.append({
                    "name": food["name"], 
                    "price": food["price"], 
                    "restaurant": food["restaurant"],
                    "tags_string": ", ".join(food["tags"]) 
                })
            
            # Add to collection in one batch
            _collection.add(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)
            print("✅ Indexing complete! Future starts will be instant.")
            
    return _collection

def retrieve_foods(query_keywords: list, user_text: str, top_k: int = 3, target_price: int = 150):
    try:
        model = _get_model()
        collection = _get_collection()
        
        # 0. PRE-FETCH RATINGS
        # We fetch this once at the start to avoid multiple slow file reads
        ratings_map = get_food_ratings_summary()

        # 1. CLEAN USER TEXT
        fluff = {"i", "am", "want", "to", "eat", "a", "the", "feeling", "really", "and", "very", "tired", "stressed"}
        user_words = [w.lower() for w in re.findall(r'\w+', user_text) if w.lower() not in fluff]
        
        # 2. CREATE BALANCED QUERY
        search_query = f"{' '.join(user_words * 3)} {' '.join(query_keywords)}"
        query_embedding = model.encode(search_query).tolist()

        # Fetch candidates for re-ranking
        results = collection.query(
            query_embeddings=[query_embedding], 
            n_results=min(40, len(FOOD_DATA))
        )

        scored_candidates = []
        for i, metadata in enumerate(results["metadatas"][0]):
            item_price = metadata["price"]
            item_name = metadata["name"]
            item_tags = metadata["tags_string"].lower().split(", ")
            
            # A. SEMANTIC SCORE (Vector similarity)
            semantic_score = 1 - results["distances"][0][i] 

            # B. NAME MATCH BOOST (Direct request priority)
            name_boost = 0
            for word in user_words:
                if len(word) > 2 and word.lower() in item_name.lower():
                    name_boost += 0.5

            # C. VIBE MATCH SCORE (Sliders alignment)
            vibe_matches = 0
            if query_keywords:
                for vibe_tag in query_keywords:
                    if vibe_tag.lower() in item_tags:
                        vibe_matches += 1
                vibe_score = vibe_matches / len(query_keywords)
            else:
                vibe_score = 0

            # D. PRICE PROXIMITY SCORE
            price_diff = abs(item_price - target_price)
            price_score = 1 / (1 + (price_diff / 40)) 

            # E. RATING DATA & BOOST
            # Fetch community rating for this specific item
            rating_info = ratings_map.get(item_name, {"avg": 0, "count": 0})
            avg_rating = rating_info["avg"]
            rating_count = rating_info["count"]
            
            # Rating Boost: Give a small 10% bonus if the food has 4+ stars
            rating_boost = 0.1 if avg_rating >= 4.0 else 0

            # F. FINAL HYBRID RANKING
            # 30% Name Match | 20% Vibe | 20% Semantic | 10% Price | 20% Popularity
            final_score = (name_boost * 0.3) + (vibe_score * 0.2) + \
                          (semantic_score * 0.2) + (price_score * 0.1) + (rating_boost * 0.2)

            # Filter: Allow 25% margin over budget
            if item_price <= (target_price * 1.25):
                scored_candidates.append({
                    "name": item_name,
                    "price": item_price,
                    "restaurant": metadata["restaurant"],
                    "tags": item_tags,
                    "score": round(final_score, 3),
                    "avg_rating": avg_rating,     # For UI
                    "rating_count": rating_count  # For UI
                })

        # Sort by the final hybrid score (Direct matches + Sliders + Ratings)
        scored_candidates.sort(key=lambda x: x['score'], reverse=True)

        return scored_candidates[:top_k]

    except Exception as e:
        print(f"Retrieval Error: {e}")
        return _fallback_retrieval(query_keywords + user_words, top_k, target_price)

def _fallback_retrieval(keywords: list, top_k: int, target_price: int) -> list:
    """Enhanced fallback that handles price and keyword matching."""
    scored = []
    for food in FOOD_DATA:
        # Check Name and Tags
        content = (food["name"] + " " + " ".join(food["tags"])).lower()
        match_count = sum(1 for kw in keywords if kw.lower() in content)
        
        # Price proximity
        price_score = 1 / (1 + (abs(food["price"] - target_price) / 50))
        
        final_score = (match_count * 0.5) + (price_score * 0.5)
        
        if food["price"] <= target_price * 1.3:
            scored.append({**food, "score": round(final_score, 2)})
            
    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_k]


def get_trending_foods(top_k: int = 5) -> list:
    """Mock trending function - can be connected to feedback DB later."""
    return sorted(FOOD_DATA, key=lambda x: x.get('price', 0))[:top_k]

def init_vector_db():
    """Initializes the DB at startup to avoid delay on first request."""
    print("Pre-loading MoodBite Vector Database...")
    _get_collection()