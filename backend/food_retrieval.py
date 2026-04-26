"""
Vector DB + Food Retrieval
Smart Food Recommender — Emotion-Aware Analysis
CSU2217 | Yogananda School of AI, Shoolini University

Real menu data from restaurants near Shoolini University, Solan.
Uses ChromaDB for local vector storage + sentence-transformers for embeddings.
"""

import chromadb
from sentence_transformers import SentenceTransformer
import os

# Initialize embedding model and ChromaDB client
_model = None
_collection = None

FOOD_DATA = [
    {"name": "Dal Tadka", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 80, "restaurant": "Shoolini Dhaba"},
    {"name": "Paneer Butter Masala", "tags": ["rich", "comforting", "high protein", "filling"], "price": 120, "restaurant": "Shoolini Dhaba"},
    {"name": "Chole Bhature", "tags": ["filling", "energizing", "spicy"], "price": 70, "restaurant": "Solan Canteen"},
    {"name": "Aloo Paratha", "tags": ["quick", "comforting", "home-style", "simple"], "price": 50, "restaurant": "Solan Canteen"},
    {"name": "Banana Shake", "tags": ["high protein", "quick", "energizing", "light"], "price": 60, "restaurant": "Campus Juice Corner"},
    {"name": "Moong Dal Chilla", "tags": ["light", "healthy", "quick", "simple"], "price": 60, "restaurant": "Health Bites"},
    {"name": "Masala Oats", "tags": ["light", "nutritious", "quick", "balanced"], "price": 55, "restaurant": "Health Bites"},
    {"name": "Rajma Chawal", "tags": ["warm", "comforting", "filling", "home-style"], "price": 90, "restaurant": "Shoolini Dhaba"},
    {"name": "Fruit Bowl", "tags": ["fresh", "light", "healthy", "variety"], "price": 80, "restaurant": "Campus Juice Corner"},
    {"name": "Maggi Noodles", "tags": ["quick", "simple", "comfort food"], "price": 40, "restaurant": "Solan Canteen"},
    {"name": "Grilled Sandwich", "tags": ["moderate", "balanced", "quick"], "price": 65, "restaurant": "Campus Café"},
    {"name": "Poha", "tags": ["light", "simple", "easy to digest", "quick"], "price": 35, "restaurant": "Solan Canteen"},
    {"name": "Pav Bhaji", "tags": ["filling", "comforting", "warm", "spicy"], "price": 75, "restaurant": "Campus Café"},
    {"name": "Sprouts Salad", "tags": ["high protein", "fresh", "light", "healthy"], "price": 70, "restaurant": "Health Bites"},
    {"name": "Khichdi", "tags": ["soothing", "easy to digest", "warm", "comforting"], "price": 65, "restaurant": "Shoolini Dhaba"},
]


def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _get_collection():
    global _collection
    if _collection is None:
        client = chromadb.Client()
        _collection = client.get_or_create_collection("moodbite_foods")

        if _collection.count() == 0:
            model = _get_model()
            for i, food in enumerate(FOOD_DATA):
                tag_text = " ".join(food["tags"])
                embedding = model.encode(tag_text).tolist()
                _collection.add(
                    ids=[str(i)],
                    embeddings=[embedding],
                    documents=[tag_text],
                    metadatas=[{"name": food["name"], "price": food["price"], "restaurant": food["restaurant"]}]
                )
    return _collection


def retrieve_foods(keywords: list, top_k: int = 3, max_price: int = 1000) -> list:
    """Retrieve top food matches and filter by budget."""
    try:
        model = _get_model()
        collection = _get_collection()

        query_text = " ".join(keywords)
        query_embedding = model.encode(query_text).tolist()

        # We fetch more than top_k initially so we have enough items 
        # to filter by price afterwards
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=min(10, len(FOOD_DATA)) 
        )

        foods = []
        for i, metadata in enumerate(results["metadatas"][0]):
            # BUDGET FILTER LOGIC:
            if metadata["price"] <= max_price:
                foods.append({
                    "name": metadata["name"],
                    "price": metadata["price"],
                    "restaurant": metadata["restaurant"],
                    "score": round(1 - results["distances"][0][i], 3)
                })
        
        # Return only the top_k results that fit the budget
        return foods[:top_k]

    except Exception as e:
        print(f"ChromaDB error: {e}")
        return _fallback_retrieval(keywords, top_k)


def _fallback_retrieval(keywords: list, top_k: int = 3) -> list:
    """Simple keyword-match fallback when vector DB is unavailable."""
    scored = []
    for food in FOOD_DATA:
        score = sum(1 for kw in keywords if any(kw.lower() in tag.lower() for tag in food["tags"]))
        scored.append((score, food))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [
        {"name": f["name"], "price": f["price"], "restaurant": f["restaurant"], "score": s}
        for s, f in scored[:top_k]
    ]
