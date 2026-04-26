# -*- coding: utf-8 -*-
# MoodBite - Updated Flask Backend Server

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from emotion_engine.pipeline import process_user_input 
from food_retrieval import retrieve_foods
from ai_services import generate_ai_response
from data_storage import (
    save_profile, get_profile, save_feedback, get_feedback,
    save_history, get_history, get_user_stats
)
import json

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), "..", "frontend"))
CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "app.html")

@app.route("/api/analyse", methods=["POST"])
def analyse():
    data = request.get_json()
    
    # 1. Extract raw data from the UI
    mood_text = data.get("mood_text", "")
    budget = int(data.get("budget", 150))
    user_id = data.get("user_id", "anonymous")
    
    # 2. Run Pipeline
    result = process_user_input(data) 
    
    # 3. Enhance keywords based on the Vent Box
    keywords = result["food_intent"]["keywords"]
    if "long day" in mood_text.lower() or "tired" in mood_text.lower():
        keywords.append("comforting")
    
    # 4. Get budget-aware foods
    foods = retrieve_foods(keywords, top_k=3, max_price=budget)
    
    # 5. Generate AI Explanation
    ai_response = generate_ai_response(result["mood"], result["energy_level"], foods)
    
    # 6. Save to history (if user_id provided)
    if user_id and user_id != "anonymous":
        history_data = {
            "mood": result["mood"],
            "energy_score": result["energy_score"],
            "energy_level": result["energy_level"],
            "food_type": result["food_intent"]["food_type"],
            "keywords": keywords,
            "foods": foods,
            "budget": budget
        }
        save_history(user_id, history_data)
    
    return jsonify({
        "mood": result["mood"],
        "foods": foods,
        "ai_response": ai_response,
        "keywords": keywords
    })

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

@app.route("/api/stats/<user_id>", methods=["GET"])
def api_get_stats(user_id):
    """Get statistics for a user"""
    stats = get_user_stats(user_id)
    return jsonify({"success": True, "stats": stats})

if __name__ == "__main__":
    app.run(debug=True, port=5000)