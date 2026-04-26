"""Standalone pipeline runner — useful for testing without Streamlit."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from emotion_engine.pipeline import process_user_input

if __name__ == "__main__":
    sample_answers = {
        "q1": "B",  # Stressed
        "q2": "C",  # Low energy
        "q3": "D",  # Very high stress
        "q4": "C",  # A bit distracted
        "q5": "C",  # Low motivation to cook
    }

    result = process_user_input(sample_answers)
    print("=== MoodBite Pipeline Output ===")
    print(f"Mood:         {result['mood']}")
    print(f"Energy Score: {result['energy_score']}/100")
    print(f"Energy Level: {result['energy_level']}")
    print(f"Food Type:    {result['food_intent']['food_type']}")
    print(f"Keywords:     {', '.join(result['food_intent']['keywords'])}")
