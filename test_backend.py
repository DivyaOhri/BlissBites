import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend/src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from food_retrieval import retrieve_foods
from ai_services import generate_ai_response

print("--- 1. Testing ChromaDB ---")
foods = retrieve_foods(["warm", "spicy"], top_k=2, max_price=100)
print(f"Found: {[f['name'] for f in foods]}")

print("\n--- 2. Testing Gemini AI ---")
explanation = generate_ai_response("stressed", "low", foods)
print(explanation)