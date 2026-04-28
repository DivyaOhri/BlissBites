# -*- coding: utf-8 -*-
import sys, os

# Ensure the backend and src folders are in the system path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json

# --- THE FIX: IMPORT FROM THE NEW DATA FILE ---
from food_data import FOOD_DATA 
from food_retrieval import retrieve_foods, init_vector_db
from emotion_engine.pipeline import process_user_input 
from ai_services import generate_ai_response
from data_storage import (
    save_profile, get_profile, save_feedback, get_feedback,
    save_history, get_history, get_user_stats
)

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), "..", "frontend"))
CORS(app)

# Initialize the Vector DB at startup so it's ready for the presentation
with app.app_context():
    try:
        init_vector_db()
    except Exception as e:
        print(f"⚠️ Vector DB Setup Error: {e}")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "app.html")

@app.route("/api/analyse", methods=["POST"])
def analyse():
    data = request.get_json()
    
    # 1. EXTRACT DATA
    user_text = data.get("text_input", "")
    budget = int(data.get("budget", 150))
    stress_val = int(data.get("stress", 5))   # New: Get stress slider (0-10)
    energy_val = int(data.get("energy", 5))   # New: Get energy slider (0-10)
    
    # 2. RUN PIPELINE (Get base mood)
    result = process_user_input(data) 
    mood = result["mood"]
    
    # 3. DYNAMIC VIBE MAPPING
    # We turn the slider numbers into actual food tags
    vibe_tags = []
    
    # Stress Mapping: High stress needs comfort/rich food
    if stress_val >= 7:
        vibe_tags.extend(["comfort food", "indulgent", "rich", "snack"])
    
    # Energy Mapping: Low energy needs light food; High energy needs filling food
    if energy_val <= 3:
        vibe_tags.extend(["light", "simple", "quick", "easy to digest"])
    elif energy_val >= 8:
        vibe_tags.extend(["filling", "high protein", "energizing", "loaded"])
    
    # Mood Mapping: Specific cravings for specific moods
    mood_map = {
        "happy": ["classic", "celebratory", "variety"],
        "sad": ["warm", "comforting", "home-style"],
        "tired": ["quick", "simple", "energizing"],
        "angry": ["spicy", "bold", "crispy"]
    }
    vibe_tags.extend(mood_map.get(mood.lower(), ["balanced"]))

    # 4. HYBRID SEARCH
    # We combine the vibe_tags with the pipeline's keywords
    query_keywords = list(set(vibe_tags + result["food_intent"]["keywords"]))
    
    foods = retrieve_foods(
        query_keywords=query_keywords, 
        user_text=user_text, 
        top_k=3, 
        target_price=budget
    )
    
    # 5. AI INSIGHTS
    ai_response = generate_ai_response(result["mood"], result["energy_level"], foods)
    
    return jsonify({
        "mood_analysis": {
            "label": result["mood"].capitalize(),
            "explanation": ai_response,
            "tags": query_keywords # Now shows the dynamic vibe tags!
        },
        "foods": foods
    })

    app.run(debug=True, port=5000)
# ==================== PROFILE ENDPOINTS ====================

@app.route("/api/profile/save", methods=["POST"])
def api_save_profile():
    """Save user profile"""
    data = request.get_json()
    user_id = data.get("user_id", "anonymous")
    profile_data = data.get("profile", {})
    
    result = save_profile(user_id, profile_data)
    return jsonify(result)

@app.route("/api/profile/<user_id>", methods=["GET"])
def api_get_profile(user_id):
    """Get user profile"""
    profile = get_profile(user_id)
    if profile:
        return jsonify({"success": True, "profile": profile})
    return jsonify({"success": False, "message": "Profile not found"})

# ==================== FEEDBACK ENDPOINTS ====================

@app.route("/api/feedback", methods=["POST"])
def api_save_feedback():
    """Save feedback for a food recommendation"""
    data = request.get_json()
    result = save_feedback(data)
    return jsonify(result)

@app.route("/api/feedback/<user_id>", methods=["GET"])
def api_get_feedback(user_id):
    """Get feedback for a user"""
    feedback = get_feedback(user_id)
    return jsonify({"success": True, "feedback": feedback})

# ==================== HISTORY ENDPOINTS ====================

@app.route("/api/history/<user_id>", methods=["GET"])
def api_get_history(user_id):
    """Get mood/food history for a user"""
    limit = request.args.get("limit", 10, type=int)
    history = get_history(user_id, limit)
    return jsonify({"success": True, "history": history})

@app.route("/api/history", methods=["POST"])
def api_save_history():
    """Save mood/food history entry"""
    data = request.get_json()
    user_id = data.get("user_id", "anonymous")
    history_data = {
        "mood": data.get("mood", ""),
        "energy": data.get("energy", ""),
        "foods": data.get("foods", []),
        "stress": data.get("stress", 5),
        "budget": data.get("budget", 150)
    }
    result = save_history(user_id, history_data)
    return jsonify(result)

@app.route("/api/stats/<user_id>", methods=["GET"])
def api_get_stats(user_id):
    """Get statistics for a user"""
    stats = get_user_stats(user_id)
    return jsonify({"success": True, "stats": stats})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

