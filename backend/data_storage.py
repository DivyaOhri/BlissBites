# -*- coding: utf-8 -*-
"""
Data Storage Module for MoodBite
Handles persistent storage for user profiles and mood/food history
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
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ==================== PROFILE MANAGEMENT ====================

def save_profile(user_id: str, profile_data: Dict) -> Dict:
    """
    Save or update user profile.
    
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
    Save user feedback for a food recommendation.
    
    Args:
        feedback_data: Dict with keys like user_id, food_name, rating, comment
    
    Returns:
        Dict with success status and message
    """
    feedback_list = _load_json(FEEDBACK_FILE, [])
    
    # Add timestamp
    feedback_data["timestamp"] = datetime.now().isoformat()
    feedback_data["id"] = len(feedback_list) + 1
    
    feedback_list.append(feedback_data)
    _save_json(FEEDBACK_FILE, feedback_list)
    
    return {"success": True, "message": "Feedback saved", "feedback_id": feedback_data["id"]}


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