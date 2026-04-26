# -*- coding: utf-8 -*-
# MoodBite - Eat What You Feel
# Full Streamlit App - all 8 pages, matching app.html design.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

import streamlit as st
import requests
from emotion_engine import process_user_input, QUESTIONNAIRE
from food_retrieval import retrieve_foods
from ai_services import generate_ai_response

# Backend API URL
API_BASE = "http://localhost:5000"

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BlissBites — Eat What You Feel",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── GLOBAL CSS (matches app.html palette + typography) ────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --cream: #FFF9F3; --peach-light: #FDEEE0; --peach: #F9D4B0;
  --orange: #E8732A; --orange-deep: #C4561A; --amber: #F4A646;
  --rose: #E8556A; --green: #5BAF6E; --teal: #3AACA8;
  --lavender: #9B8EC4; --charcoal: #2A2420; --brown: #5C4033;
  --warm-gray: #8A7A72; --card-shadow: 0 16px 48px rgba(90,50,20,0.10);
}

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background: var(--cream); }
h1, h2, h3, h4 { font-family: 'Cormorant Garamond', serif !important; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fff8f3 !important;
    border-right: 1px solid #f9d4b0;
}
section[data-testid="stSidebar"] .stSelectbox label {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem; font-weight: 700; color: #2A2420;
}

/* Hero */
.hero-banner {
    background: linear-gradient(135deg, #E8732A 0%, #E8556A 100%);
    border-radius: 28px; padding: 52px 48px; color: white;
    margin-bottom: 36px; box-shadow: 0 16px 48px rgba(232,115,42,0.35);
    text-align: center;
}
.hero-banner h1 { color: white !important; font-size: 3rem !important; margin-bottom: 12px; }
.hero-banner p  { font-size: 1.1rem; opacity: 0.93; line-height: 1.8; }

/* Stat cards */
.stat-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 16px; margin-bottom: 32px; }
.stat-box {
    background: white; border-radius: 20px; padding: 24px;
    text-align: center; box-shadow: var(--card-shadow);
}
.stat-num { font-family: 'Cormorant Garamond',serif; font-size: 2.4rem; font-weight:700; color: var(--orange); }
.stat-lbl { font-size: 0.82rem; color: var(--warm-gray); font-weight:500; margin-top:4px; }

/* Feature cards */
.feat-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; margin-bottom: 36px; }
.feat-card {
    background: white; border-radius: 20px; padding: 28px 22px;
    box-shadow: var(--card-shadow); border-top: 4px solid var(--orange);
}
.feat-card h3 { font-size: 1.2rem !important; margin-bottom: 8px; color: var(--charcoal); }
.feat-card p  { font-size: 0.9rem; color: var(--warm-gray); line-height: 1.7; }

/* Steps */
.steps-wrap { background: var(--peach-light); border-radius: 24px; padding: 40px; margin-bottom: 32px; }
.steps-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
.step-box  { text-align: center; }
.step-num  {
    width:48px; height:48px; border-radius:50%;
    background: linear-gradient(135deg, var(--orange), var(--rose));
    color: white; font-size: 1.3rem; font-weight:700;
    display:flex; align-items:center; justify-content:center;
    margin: 0 auto 12px;
    font-family: 'Cormorant Garamond',serif;
}
.step-box h4 { font-size: 1rem !important; color: var(--charcoal); margin-bottom:6px; }
.step-box p  { font-size: 0.85rem; color: var(--warm-gray); line-height:1.6; }

/* Panel / white card */
.panel {
    background: white; border-radius: 20px; padding: 28px 32px;
    box-shadow: var(--card-shadow); margin-bottom: 20px;
}
.panel-title { font-family:'Cormorant Garamond',serif; font-size:1.2rem; font-weight:700; color:var(--charcoal); margin-bottom:16px; }

/* Mood grid */
.mood-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 12px; }
.mood-btn {
    background: var(--cream); border: 2px solid var(--peach);
    border-radius: 16px; padding: 16px 10px; text-align: center;
    cursor: pointer; transition: all 0.2s;
}
.mood-btn.sel { border-color: var(--orange); background: var(--peach-light); }
.mood-btn .me { font-size: 2rem; }
.mood-btn .ml { font-size: 0.82rem; font-weight:600; color:var(--charcoal); margin-top:4px; }

/* Meter */
.meter-row { display: grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:20px; }
.meter-card { background:white; border-radius:20px; padding:24px; box-shadow:var(--card-shadow); }
.meter-lbl  { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:700; color:var(--charcoal); margin-bottom:10px; }
.meter-val  { font-family:'Cormorant Garamond',serif; font-size:2.8rem; font-weight:700; color:var(--orange); }
.meter-bar-bg { height:8px; background:var(--peach); border-radius:4px; overflow:hidden; margin-top:10px; }
.meter-bar-fill { height:100%; border-radius:4px; background:linear-gradient(90deg,var(--orange),var(--amber)); }

/* AI explain box */
.ai-box {
    background: linear-gradient(135deg,#FFF8F0,#FDEEE0);
    border-left: 5px solid var(--orange);
    border-radius: 0 16px 16px 0;
    padding: 24px 28px; margin-bottom:20px;
}
.ai-box h4 { font-size:1rem; font-weight:700; color:var(--charcoal); margin-bottom:8px; }
.ai-box p  { font-size:0.95rem; color:var(--brown); line-height:1.75; }

/* Tags */
.tag {
    display:inline-block; background:var(--peach-light); color:var(--orange-deep);
    font-size:0.78rem; font-weight:600; padding:6px 14px; border-radius:20px; margin:4px;
}

/* Wellness tip */
.tip-box {
    background:white; border-radius:16px; padding:18px 22px;
    box-shadow:var(--card-shadow); display:flex; gap:12px;
    align-items:flex-start; margin-top:16px;
}
.tip-box p { font-size:0.9rem; color:var(--brown); line-height:1.7; }

/* Result cards */
.res-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; margin-bottom:24px; }
.res-card {
    background:white; border-radius:22px; padding:26px 20px;
    box-shadow:var(--card-shadow); text-align:center;
    border-top:4px solid var(--amber); transition:all 0.3s;
}
.res-card:nth-child(2) { border-top-color: var(--green); }
.res-card:nth-child(3) { border-top-color: var(--teal); }
.res-rank   { font-size:0.72rem; font-weight:700; letter-spacing:1px; color:var(--warm-gray); text-transform:uppercase; margin-bottom:10px; }
.res-emoji  { font-size:3rem; margin-bottom:10px; }
.res-name   { font-family:'Cormorant Garamond',serif; font-size:1.25rem; font-weight:700; color:var(--charcoal); margin-bottom:4px; }
.res-place  { font-size:0.82rem; color:var(--warm-gray); margin-bottom:10px; }
.res-desc   { font-size:0.85rem; color:var(--brown); line-height:1.65; margin-bottom:12px; }
.res-price  { font-family:'Cormorant Garamond',serif; font-size:1.9rem; font-weight:700; color:var(--orange); }
.res-save   { font-size:0.78rem; color:var(--green); font-weight:600; }

/* Summary dark bar */
.sum-bar {
    background:linear-gradient(135deg,#2A2420,#1A1610);
    border-radius:18px; padding:26px 32px;
    display:flex; align-items:center; gap:24px;
    margin-bottom:20px;
}
.sum-bar-info h4 { font-family:'Cormorant Garamond',serif; color:white; font-size:1.1rem; margin-bottom:4px; }
.sum-bar-info p  { font-size:0.88rem; color:rgba(255,255,255,0.75); }
.sum-price { text-align:center; margin-left:auto; }
.sum-price-num { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:700; color:#F4A646; }
.sum-price-lbl { font-size:0.72rem; color:rgba(255,255,255,0.5); }

/* Budget boxes */
.bud-trio { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:24px; }
.bud-box  { border-radius:18px; padding:24px; text-align:center; box-shadow:var(--card-shadow); }
.bud-icon { font-size:1.6rem; margin-bottom:8px; }
.bud-lbl  { font-size:0.82rem; color:var(--warm-gray); margin-bottom:6px; }
.bud-val  { font-family:'Cormorant Garamond',serif; font-size:2.2rem; font-weight:700; }

/* Comparison row */
.comp-row {
    background:white; border-radius:12px; padding:16px 20px;
    display:flex; align-items:center; gap:14px;
    box-shadow:0 4px 16px rgba(90,50,20,0.07); margin-bottom:10px;
}
.comp-name { font-weight:600; color:var(--charcoal); font-size:0.9rem; }
.comp-place{ font-size:0.76rem; color:var(--warm-gray); margin-top:2px; }
.comp-price{ font-family:'Cormorant Garamond',serif; font-size:1.4rem; font-weight:700; }

/* Food detail card */
.food-card {
    background:white; border-radius:22px; padding:30px;
    box-shadow:var(--card-shadow); margin-bottom:20px;
    display:flex; gap:24px; border-left:5px solid var(--orange);
}
.food-emoji { font-size:4rem; flex-shrink:0; }
.food-name  { font-family:'Cormorant Garamond',serif; font-size:1.5rem; font-weight:700; color:var(--charcoal); margin-bottom:4px; }
.food-meta  { font-size:0.85rem; color:var(--warm-gray); margin-bottom:10px; }
.food-desc  { font-size:0.9rem; color:var(--brown); line-height:1.7; margin-bottom:12px; }
.food-price { font-family:'Cormorant Garamond',serif; font-size:1.9rem; font-weight:700; color:var(--orange); }

.science-box {
    background:linear-gradient(135deg,#F0FAF5,#D4F5E9);
    border-radius:16px; padding:22px 26px;
    border-left:5px solid var(--green); margin-top:20px;
}
.science-box h4 { font-size:1rem; font-weight:700; color:var(--charcoal); margin-bottom:8px; }
.science-box p  { font-size:0.9rem; color:#3A6A4A; line-height:1.7; }

/* Profile */
.avatar-card {
    background:white; border-radius:24px; padding:30px 20px;
    text-align:center; box-shadow:var(--card-shadow);
}
.avatar-circle {
    width:90px; height:90px; border-radius:50%;
    background:linear-gradient(135deg,var(--orange),var(--rose));
    display:flex; align-items:center; justify-content:center;
    margin:0 auto 14px;
    font-family:'Cormorant Garamond',serif; font-size:2.4rem; font-weight:700; color:white;
}
.avatar-name { font-family:'Cormorant Garamond',serif; font-size:1.3rem; font-weight:700; color:var(--charcoal); }
.avatar-uni  { font-size:0.82rem; color:var(--warm-gray); }

.badge-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:16px; }
.badge-card { border-radius:14px; padding:16px; text-align:center; }
.badge-icon { font-size:1.6rem; }
.badge-lbl  { font-size:0.76rem; font-weight:600; color:var(--charcoal); margin-top:4px; }

/* About */
.about-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:24px; }
.about-card { background:white; border-radius:18px; padding:28px; box-shadow:var(--card-shadow); }
.about-card h3 { font-size:1.1rem !important; font-weight:700; color:var(--charcoal); margin-bottom:12px; }
.about-card li { font-size:0.9rem; color:var(--brown); line-height:2; }

.wellness-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:28px; }
.wellness-card { border-radius:14px; padding:20px 24px; }
.wellness-card h4 { font-size:0.95rem !important; font-weight:700; color:var(--charcoal); margin-bottom:10px; }
.wellness-card li { font-size:0.85rem; color:var(--brown); line-height:1.9; }

.team-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:24px; }
.team-card { border-radius:14px; padding:20px 12px; text-align:center; }
.team-init { width:52px; height:52px; border-radius:50%;
    background:linear-gradient(135deg,var(--orange),var(--rose));
    color:white; font-family:'Cormorant Garamond',serif; font-size:1.3rem; font-weight:700;
    display:flex; align-items:center; justify-content:center; margin:0 auto 10px; }
.team-name { font-weight:600; color:var(--charcoal); font-size:0.88rem; margin-bottom:2px; }
.team-reg  { font-size:0.74rem; color:var(--warm-gray); margin-bottom:6px; }
.team-role { font-size:0.78rem; color:var(--orange); font-weight:600; }

/* Stray Streamlit elements */
div[data-testid="stRadio"] > label { font-weight: 600; color: var(--charcoal); }
.stButton > button {
    border-radius: 50px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
}
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── MOOD META ─────────────────────────────────────────────────────────────────
MOOD_META = {
    "happy":      {"icon":"😊","label":"Happy & Energetic","bg":"#D4F5E9","accent":"#2ECC71",
                   "tagline":"You're radiating good vibes today!",
                   "tags":["fun","fresh","indulgent","energy"],
                   "tip":"🌱 Your positive state boosts taste perception — try something new today!",
                   "science":"When happy, your palate is more adventurous. Bold, exciting flavours enhance and extend positive emotions.",
                   "encourage":"🌟 Keep that energy going — you deserve the best today!"},
    "stressed":   {"icon":"😰","label":"Stressed","bg":"#FFE4CC","accent":"#FF8C42",
                   "tagline":"Take a breath — food can help.",
                   "tags":["comfort","warm","soothing","light"],
                   "tip":"🍵 Warm foods trigger serotonin release. Avoid caffeine on an empty stomach.",
                   "science":"Warm carbohydrate-rich foods stimulate serotonin production, reducing cortisol — the stress hormone.",
                   "encourage":"💙 Remember: nourishing yourself is an act of self-care. You've got this."},
    "tired":      {"icon":"😴","label":"Low Energy","bg":"#E8EAFF","accent":"#7C5CFC",
                   "tagline":"Your body's asking for rest and nourishment.",
                   "tags":["light","warm","easy","comfort"],
                   "tip":"💧 Stay hydrated. Light, easily digestible meals prevent energy crashes.",
                   "science":"Light, easily digestible foods prevent your body from using extra energy on digestion, restoring you faster.",
                   "encourage":"🌸 Rest, eat well, and be kind to yourself. Tomorrow is a new day."},
    "anxious":    {"icon":"😟","label":"Anxious","bg":"#FFF0E0","accent":"#FF8C42",
                   "tagline":"Familiar comfort is what you need.",
                   "tags":["comfort","soothing","warm","simple"],
                   "tip":"🌸 Familiar foods reduce cortisol. Avoid excessive spice when anxious.",
                   "science":"Familiar comfort foods activate the brain's reward system, providing psychological safety and stability.",
                   "encourage":"🌿 One meal at a time. You're doing great just by taking care of yourself."},
    "neutral":    {"icon":"😐","label":"Neutral / Just Hungry","bg":"#F0F0F0","accent":"#888888",
                   "tagline":"Just hungry? That's perfectly fine!",
                   "tags":["filling","comfort","quick"],
                   "tip":"⚖️ A balanced meal keeps your mood stable throughout the day.",
                   "science":"A balanced meal stabilises blood sugar, keeping your mood even and your focus sharp.",
                   "encourage":"⭐ Eating well is always a good decision. Enjoy!"},
    "sad":        {"icon":"😢","label":"Sad","bg":"#E8EAFF","accent":"#7C5CFC",
                   "tagline":"Comfort food coming right up.",
                   "tags":["comfort","warm","soothing","sweet"],
                   "tip":"🍫 Comfort food and warm drinks can gently lift your spirits.",
                   "science":"Warm, sweet foods can mildly elevate serotonin levels, providing a gentle mood lift.",
                   "encourage":"💜 Be gentle with yourself. Every bite is a small act of self-care."},
}

FOOD_ICONS = {
    "Pizza":"🍕","Momos":"🥟","Chai":"☕","Cold Coffee":"🧋","Soup":"🍲",
    "Maggi":"🍜","Pasta":"🍝","South Indian":"🫓","Paratha":"🫓","Burger":"🍔",
    "Thali":"🍱","Shake":"🥤","Noodles":"🍜","Juice":"🥤","Chinese":"🥡",
    "Indian":"🍛","Snacks":"🍟","Hot Coffee":"☕","Meal Deal":"🍱","Bakery":"🥐",
}

def food_icon(food_name: str) -> str:
    for k, v in FOOD_ICONS.items():
        if k.lower() in food_name.lower():
            return v
    return "🍽️"

# ── SESSION STATE DEFAULTS ────────────────────────────────────────────────────
for k, d in [("result", None), ("foods", []), ("ai_text", ""),
             ("mood_key", "neutral"), ("energy_score", 50), ("stress", 5),
             ("budget", 150), ("profile_name", ""), ("profile_saved", False)]:
    if k not in st.session_state:
        st.session_state[k] = d

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍜 BlissBites")
    st.markdown("*Eat What You Feel*")
    st.markdown("---")
    page = st.selectbox("Navigate", [
        "🏠 Home", "😊 Mood Check", "💡 Mood Insights",
        "💰 Budget Insights", "🍽️ Food Details",
        "👤 Profile", "✨ Results", "📖 About"
    ])
    st.markdown("---")
    st.markdown("<small style='color:#8A7A72'>CSU2217 · Shoolini University</small>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ═══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Home":
    st.markdown("""
    <div class="hero-banner">
        <div style="font-size:3.5rem;margin-bottom:12px;">🍜</div>
        <h1>Food that matches how you feel</h1>
        <p>Tell us your mood and BlissBites finds the <strong>perfect meal</strong> from cafés right around campus —
        mood-aware, budget-smart, and always local.</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="stat-row">
        <div class="stat-box"><div class="stat-num">521</div><div class="stat-lbl">Menu Items</div></div>
        <div class="stat-box"><div class="stat-num">19</div><div class="stat-lbl">Restaurants</div></div>
        <div class="stat-box"><div class="stat-num">7</div><div class="stat-lbl">Mood Types</div></div>
        <div class="stat-box"><div class="stat-num">100%</div><div class="stat-lbl">Local Data</div></div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="feat-grid">
        <div class="feat-card">
            <div style="font-size:1.8rem;margin-bottom:10px;">🧠</div>
            <h3>Mood-Aware AI</h3>
            <p>We read your emotional and physical state and match food to how you actually feel — not just what's trending.</p>
        </div>
        <div class="feat-card" style="border-top-color:#5BAF6E;">
            <div style="font-size:1.8rem;margin-bottom:10px;">📍</div>
            <h3>Truly Local</h3>
            <p>521 real menu items from 19 restaurants around Shoolini campus. Every recommendation is walkable from your lecture hall.</p>
        </div>
        <div class="feat-card" style="border-top-color:#9B8EC4;">
            <div style="font-size:1.8rem;margin-bottom:10px;">💸</div>
            <h3>Budget Smart</h3>
            <p>Set your budget ceiling — we'll only show you what you can actually afford, with savings displayed on every pick.</p>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="steps-wrap">
        <h2 style="text-align:center;margin-bottom:32px;font-size:1.8rem;">How it works in 3 steps ✨</h2>
        <div class="steps-grid">
            <div class="step-box">
                <div class="step-num">1</div>
                <div style="font-size:2rem;margin-bottom:8px;">🙂</div>
                <h4>Tell us your mood</h4>
                <p>Answer 5 quick questions about your emotional state, stress, energy, and budget. Takes 30 seconds.</p>
            </div>
            <div class="step-box">
                <div class="step-num">2</div>
                <div style="font-size:2rem;margin-bottom:8px;">🔍</div>
                <h4>AI finds your match</h4>
                <p>Our pipeline maps your emotional profile to the most fitting food using semantic vector search.</p>
            </div>
            <div class="step-box">
                <div class="step-num">3</div>
                <div style="font-size:2rem;margin-bottom:8px;">🍽️</div>
                <h4>Enjoy your meal</h4>
                <p>Get personalised picks with full explanations, locations, and price breakdowns. Walk over and eat!</p>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: MOOD CHECK
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "😊 Mood Check":
    st.title("😊 Mood Check")
    st.markdown("Let's understand how you're feeling right now — takes about 30 seconds!")
    st.markdown("---")

    # Mood picker
    st.markdown('<div class="panel"><div class="panel-title">🎭 How are you feeling right now?</div>', unsafe_allow_html=True)
    moods = [
        ("happy","😊","Happy & Energetic"),("stressed","😰","Stressed"),
        ("tired","😴","Tired & Low Energy"),("anxious","😟","Anxious & Uneasy"),
        ("neutral","😐","Neutral / Just Hungry"),("sad","😢","Sad or Low"),
    ]
    cols = st.columns(3)
    for i, (key, emoji, label) in enumerate(moods):
        with cols[i % 3]:
            if st.button(f"{emoji}\n{label}", key=f"mood_{key}", use_container_width=True):
                st.session_state["mood_key"] = key
    selected_mood = st.session_state.get("mood_key", "neutral")
    md = MOOD_META.get(selected_mood, MOOD_META["neutral"])
    st.success(f"{md['icon']} Selected: **{md['label']}** — {md['tagline']}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Stress slider
    st.markdown('<div class="panel"><div class="panel-title">🌡️ Stress level right now</div>', unsafe_allow_html=True)
    stress = st.slider("", 1, 10, st.session_state.get("stress", 5), key="stress_slider",
                        help="1 = Totally chill · 10 = Overwhelmed")
    st.session_state["stress"] = stress
    st.markdown('</div>', unsafe_allow_html=True)

    # Energy slider
    st.markdown('<div class="panel"><div class="panel-title">⚡ Energy level (0–100)</div>', unsafe_allow_html=True)
    energy = st.slider("", 0, 100, st.session_state.get("energy_score", 50), key="energy_slider",
                        help="0 = Exhausted · 100 = Fully charged")
    st.session_state["energy_score"] = energy
    st.markdown('</div>', unsafe_allow_html=True)

    # Budget & cuisine
    st.markdown('<div class="panel"><div class="panel-title">🎯 Your Preferences</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        budget = st.number_input("💰 Budget (₹)", min_value=20, max_value=1000,
                                  value=st.session_state.get("budget", 150), step=10)
        st.session_state["budget"] = budget
    with c2:
        cuisine = st.selectbox("🍴 Cuisine (optional)",
            ["Any","Indian","Chinese","Pizza","South Indian","Maggi","Momos",
             "Burger","Pasta","Thali","Chai","Shake","Juice"])
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔍 Find My Perfect Meal →", type="primary", use_container_width=True):
        # Map mood + sliders to questionnaire answers
        mood_to_q1 = {"happy":"A","stressed":"B","sad":"C","anxious":"D",
                       "neutral":"A","tired":"C","frustrated":"B"}
        energy_to_q2 = {range(0,34):"C", range(34,67):"B", range(67,101):"A"}
        stress_to_q3 = {range(1,3):"A", range(3,6):"B", range(6,9):"C", range(9,11):"D"}

        q2 = next((v for r,v in energy_to_q2.items() if energy in r), "B")
        q3 = next((v for r,v in stress_to_q3.items() if stress in r), "B")

        answers = {
            "q1": mood_to_q1.get(selected_mood, "A"),
            "q2": q2,
            "q3": q3,
            "q4": "B",
            "q5": "B",
        }

        # Get user_id from profile (for history tracking)
        profile_name = st.session_state.get("profile_name", "")
        user_id = profile_name.lower().replace(" ", "_") if profile_name else "anonymous"

        with st.spinner("🍜 Analysing your mood..."):
            # Try to use backend API first (saves history automatically)
            try:
                response = requests.post(
                    f"{API_BASE}/api/analyse",
                    json={
                        "answers": answers,
                        "budget": budget,
                        "user_id": user_id
                    },
                    timeout=15
                )
                if response.status_code == 200:
                    api_data = response.json()
                    result = {
                        "mood": api_data.get("mood", selected_mood),
                        "energy_level": api_data.get("mood", selected_mood),
                        "food_intent": {"keywords": api_data.get("keywords", [])}
                    }
                    foods = api_data.get("foods", [])
                    ai_text = api_data.get("ai_response", "")
                else:
                    # Fallback to local processing
                    result = process_user_input(answers)
                    keywords = result["food_intent"]["keywords"]
                    foods = retrieve_foods(keywords, top_k=3)
                    ai_text = generate_ai_response(result["mood"], result["energy_level"], foods)
            except Exception as e:
                # Fallback to local processing if backend unavailable
                result = process_user_input(answers)
                keywords = result["food_intent"]["keywords"]
                foods = retrieve_foods(keywords, top_k=3)
                ai_text = generate_ai_response(result["mood"], result["energy_level"], foods)

        st.session_state["result"]       = result
        st.session_state["foods"]        = foods
        st.session_state["ai_text"]      = ai_text
        st.session_state["mood_key"]     = selected_mood
        st.session_state["stress"]       = stress
        st.session_state["energy_score"] = energy
        st.session_state["budget"]       = budget
        st.session_state["user_id"]      = user_id

        st.success("✅ Done! Navigate to **💡 Mood Insights** or **✨ Results** in the sidebar.")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: MOOD INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "💡 Mood Insights":
    st.title("💡 Mood Insights")
    st.markdown("Here's what we understood about how you're feeling.")
    st.markdown("---")

    if not st.session_state.get("result"):
        st.info("Please complete the **😊 Mood Check** first.")
    else:
        result  = st.session_state["result"]
        mood_k  = st.session_state.get("mood_key", result["mood"])
        md      = MOOD_META.get(mood_k, MOOD_META["neutral"])
        energy  = st.session_state.get("energy_score", result["energy_score"])
        stress  = st.session_state.get("stress", 5)
        tags    = md["tags"]

        # Mood hero card
        st.markdown(f"""
        <div class="panel" style="background:{md['bg']};text-align:center;padding:36px;">
            <div style="font-size:4rem;margin-bottom:10px;">{md['icon']}</div>
            <h2 style="font-size:1.9rem;color:#2A2420;">You're feeling <span style="color:{md['accent']}">{md['label']}</span></h2>
            <p style="color:#8A7A72;font-size:1rem;margin-top:6px;">{md['tagline']}</p>
        </div>""", unsafe_allow_html=True)

        # Meters
        st.markdown(f"""
        <div class="meter-row">
            <div class="meter-card">
                <div class="meter-lbl">⚡ Energy Level</div>
                <div class="meter-val">{energy}<span style="font-size:1rem;color:#8A7A72">/100</span></div>
                <div class="meter-bar-bg"><div class="meter-bar-fill" style="width:{energy}%"></div></div>
            </div>
            <div class="meter-card">
                <div class="meter-lbl">🌡️ Stress Level</div>
                <div class="meter-val">{stress}<span style="font-size:1rem;color:#8A7A72">/10</span></div>
                <div class="meter-bar-bg"><div class="meter-bar-fill" style="width:{stress*10}%;background:linear-gradient(90deg,#E8556A,#F5849A)"></div></div>
            </div>
        </div>""", unsafe_allow_html=True)

        # AI explain
        st.markdown(f"""
        <div class="ai-box">
            <h4>🤖 What this means for your food</h4>
            <p>{st.session_state.get('ai_text','').replace(chr(10),'<br>')}</p>
        </div>""", unsafe_allow_html=True)

        # Tags
        tag_html = "".join(f'<span class="tag">{t.capitalize()}</span>' for t in tags)
        st.markdown(f"<div style='margin-bottom:16px'><strong>🏷️ Food signals we're searching for</strong><br><br>{tag_html}</div>",
                    unsafe_allow_html=True)

        # Wellness tip
        st.markdown(f"""
        <div class="tip-box">
            <span style="font-size:1.4rem">🌱</span>
            <p><strong>Wellness Tip:</strong> {md['tip']}</p>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: BUDGET INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "💰 Budget Insights":
    st.title("💰 Budget Insights")
    st.markdown("Smart spending for a satisfied stomach.")
    st.markdown("---")

    foods  = st.session_state.get("foods", [])
    budget = st.session_state.get("budget", 150)

    if not foods:
        st.info("Please complete the **😊 Mood Check** first.")
    else:
        best_price = min(f["price"] for f in foods)
        savings    = budget - best_price

        st.markdown(f"""
        <div class="bud-trio">
            <div class="bud-box" style="background:linear-gradient(135deg,#FFF8F0,#FDEEE0)">
                <div class="bud-icon">💼</div><div class="bud-lbl">Your Budget</div>
                <div class="bud-val" style="color:#E8732A">₹{budget}</div>
            </div>
            <div class="bud-box" style="background:linear-gradient(135deg,#F0FAF5,#D4F5E9)">
                <div class="bud-icon">🍽️</div><div class="bud-lbl">Best Match</div>
                <div class="bud-val" style="color:#5BAF6E">₹{best_price}</div>
            </div>
            <div class="bud-box" style="background:linear-gradient(135deg,#F0F4FF,#E8EAFF)">
                <div class="bud-icon">🎉</div><div class="bud-lbl">You Save</div>
                <div class="bud-val" style="color:#9B8EC4">₹{savings}</div>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown('<div class="panel"><div class="panel-title">📊 Price comparison — your top matches</div>', unsafe_allow_html=True)
        for f in foods:
            pct   = min(int((f["price"] / budget) * 100), 100)
            color = "#5BAF6E" if pct < 60 else "#E8732A" if pct < 85 else "#E8556A"
            st.markdown(f"""
            <div class="comp-row">
                <div style="flex:1">
                    <div class="comp-name">{f['name']}</div>
                    <div class="comp-place">📍 {f['restaurant']}</div>
                </div>
                <div style="flex:2;margin:0 14px">
                    <div style="height:6px;background:#F9D4B0;border-radius:3px;overflow:hidden">
                        <div style="width:{pct}%;height:100%;background:{color};border-radius:3px"></div>
                    </div>
                </div>
                <div class="comp-price" style="color:{color}">₹{f['price']}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="panel" style="background:linear-gradient(135deg,#FFF8F0,#FDEEE0);border-left:5px solid #E8732A">
            <div class="panel-title">💡 Smart spending tips</div>
            <ul style="padding-left:20px;color:#5C4033;line-height:2.1;font-size:0.9rem">
                <li>On-campus cafés are always the cheapest option.</li>
                <li>Thali meals offer the best value — multiple items, one price.</li>
                <li>Maggi + chai combo is under ₹70 — ultimate budget meal.</li>
                <li>Look for daily specials at your nearest café for extra savings.</li>
            </ul>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: FOOD DETAILS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🍽️ Food Details":
    st.title("🍽️ Food Details")
    st.markdown("Everything you need to know about your recommended meals.")
    st.markdown("---")

    foods  = st.session_state.get("foods", [])
    mood_k = st.session_state.get("mood_key", "neutral")
    md     = MOOD_META.get(mood_k, MOOD_META["neutral"])

    if not foods:
        st.info("Please complete the **😊 Mood Check** first.")
    else:
        for f in foods:
            icon = food_icon(f["name"])
            tags_html = "".join(f'<span class="tag">{t}</span>' for t in f.get("tags", []))
            st.markdown(f"""
            <div class="food-card">
                <div class="food-emoji">{icon}</div>
                <div>
                    <div class="food-name">{f['name']}</div>
                    <div class="food-meta">🏪 {f['restaurant']}</div>
                    <div class="food-desc">A great pick for your current mood and energy level.</div>
                    <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
                        <div class="food-price">₹{f['price']}</div>
                        {tags_html}
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="science-box">
            <h4>🧪 The Food Science</h4>
            <p>{md['science']}</p>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: PROFILE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "👤 Profile":
    st.title("👤 Your Profile")
    st.markdown("Store your preferences for a more personalised experience.")
    st.markdown("---")

    col_l, col_r = st.columns([1, 2])

    with col_l:
        name = st.session_state.get("profile_name", "") or "Friend"
        initial = name[0].upper() if name else "?"
        mood_k  = st.session_state.get("mood_key", "neutral")
        md      = MOOD_META.get(mood_k, MOOD_META["neutral"])
        energy  = st.session_state.get("energy_score", 50)

        st.markdown(f"""
        <div class="avatar-card">
            <div class="avatar-circle">{initial}</div>
            <div class="avatar-name">{name}</div>
            <div class="avatar-uni">Shoolini University</div>
            {"" if not st.session_state.get("result") else f'''
            <div style="background:#FDEEE0;border-radius:14px;padding:14px;margin-top:16px">
                <div style="font-size:0.76rem;color:#8A7A72;margin-bottom:6px">Last mood check</div>
                <div style="font-size:2rem">{md['icon']}</div>
                <div style="font-weight:600;color:#2A2420;font-size:0.9rem">{md['label']}</div>
                <div style="font-size:0.76rem;color:#8A7A72;margin-top:4px">Energy: {energy}/100</div>
            </div>'''}
        </div>
        <div class="badge-grid" style="margin-top:16px">
            <div class="badge-card" style="background:#FFF3C4"><div class="badge-icon">🌟</div><div class="badge-lbl">Early Adopter</div></div>
            <div class="badge-card" style="background:#E8EAFF"><div class="badge-icon">🧠</div><div class="badge-lbl">Mood Master</div></div>
            <div class="badge-card" style="background:#D4F5E9"><div class="badge-icon">📍</div><div class="badge-lbl">Campus Explorer</div></div>
            <div class="badge-card" style="background:#D4FFE8"><div class="badge-icon">💚</div><div class="badge-lbl">Mindful Eater</div></div>
        </div>""", unsafe_allow_html=True)

    with col_r:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### ✏️ Your Preferences")
        pname    = st.text_input("Your name (optional)", value=st.session_state.get("profile_name",""), placeholder="e.g. Divya")
        pc1, pc2 = st.columns(2)
        with pc1:
            dietary = st.selectbox("Dietary type", ["Vegetarian","Vegan","Non-Vegetarian","Eggetarian"])
        with pc2:
            pref_c  = st.selectbox("Favourite cuisine", ["Any","Indian","Chinese","Italian","South Indian","Fast Food","Healthy"])
        pbgt = st.number_input("Typical budget (₹)", min_value=50, max_value=500,
                                value=st.session_state.get("budget",150), step=10)

        if st.button("💾 Save Profile", type="primary", use_container_width=True):
            # Save to session state
            st.session_state["profile_name"] = pname or "Friend"
            st.session_state["budget"]       = pbgt
            st.session_state["profile_saved"] = True
            
            # Save to backend for persistence
            user_id = pname.lower().replace(" ", "_") if pname else "anonymous"
            profile_data = {
                "name": pname or "Friend",
                "dietary": dietary,
                "cuisine": pref_c,
                "budget": pbgt
            }
            try:
                response = requests.post(
                    f"{API_BASE}/api/profile/save",
                    json={"user_id": user_id, "profile": profile_data},
                    timeout=5
                )
                if response.status_code == 200:
                    st.success(f"✅ Profile saved to cloud! Welcome, {pname or 'friend'}! 🌟")
                else:
                    st.success(f"✅ Profile saved locally! Welcome, {pname or 'friend'}! 🌟")
            except Exception as e:
                # Fallback to local-only save if backend unavailable
                st.success(f"✅ Profile saved locally! Welcome, {pname or 'friend'}! 🌟")
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "✨ Results":
    st.title("✨ Your Food Recommendations")

    if not st.session_state.get("result"):
        st.info("Please complete the **😊 Mood Check** first.")
    else:
        result  = st.session_state["result"]
        foods   = st.session_state.get("foods", [])
        ai_text = st.session_state.get("ai_text", "")
        mood_k  = st.session_state.get("mood_key", result["mood"])
        md      = MOOD_META.get(mood_k, MOOD_META["neutral"])
        budget  = st.session_state.get("budget", 150)
        pname   = st.session_state.get("profile_name","") or ""

        # Hero banner
        st.markdown(f"""
        <div class="hero-banner">
            <div style="font-size:3.5rem;margin-bottom:10px">{md['icon']}</div>
            <h1>Here's what we found{' for you, ' + pname if pname else ''}!</h1>
            <p>{md['tagline']}</p>
        </div>""", unsafe_allow_html=True)

        # Result cards
        ranks = ["🥇 Best Pick","🥈 Great Option","🥉 Also Perfect"]
        cards_html = ""
        for i, f in enumerate(foods):
            icon   = food_icon(f["name"])
            save   = budget - f["price"]
            tags_h = "".join(f'<span class="tag">{t}</span>' for t in f.get("tags",[]))
            cards_html += f"""
            <div class="res-card">
                <div class="res-rank">{ranks[i] if i < len(ranks) else '🍽️ Great Pick'}</div>
                <div class="res-emoji">{icon}</div>
                <div class="res-name">{f['name']}</div>
                <div class="res-place">📍 {f['restaurant']}</div>
                <div class="res-desc">A perfect match for your mood and energy right now.</div>
                {tags_h}
                <div style="background:#FFF9F3;border-radius:12px;padding:12px;margin-top:12px">
                    <div class="res-price">₹{f['price']}</div>
                    <div class="res-save">You save ₹{save} 💚</div>
                </div>
            </div>"""

        st.markdown(f'<div class="res-grid">{cards_html}</div>', unsafe_allow_html=True)

        # Summary dark bar
        if foods:
            best = min(foods, key=lambda x: x["price"])
            st.markdown(f"""
            <div class="sum-bar">
                <div class="sum-bar-info">
                    <h4>🎯 Our Top Recommendation</h4>
                    <p><b style="color:#FBC96A">{best['name']}</b> at <b style="color:#FBC96A">{best['restaurant']}</b>
                    fits your mood and saves you <b style="color:#8FD4A0">₹{budget - best['price']}</b>.</p>
                </div>
                <div class="sum-price">
                    <div class="sum-price-num">₹{best['price']}</div>
                    <div class="sum-price-lbl">best price</div>
                </div>
            </div>""", unsafe_allow_html=True)

        # AI explanation
        st.markdown(f"""
        <div class="ai-box">
            <h4>🤖 AI Nutritionist Says</h4>
            <p>{ai_text.replace(chr(10),'<br>')}</p>
        </div>""", unsafe_allow_html=True)

        # Encouragement
        st.markdown(f"""
        <div class="tip-box">
            <span style="font-size:1.4rem">🌟</span>
            <p>{md['encourage']}</p>
        </div>""", unsafe_allow_html=True)

        st.markdown("---")
        if st.button("🔄 Check Mood Again", use_container_width=True):
            for k in ["result","foods","ai_text"]:
                st.session_state[k] = [] if k == "foods" else (None if k == "result" else "")
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📖 About":
    st.title("📖 About BlissBites")

    st.markdown("""
    <div class="hero-banner">
        <h2 style="font-size:2rem !important">What is BlissBites? 🍜</h2>
        <p>BlissBites is a <strong>smart, emotion-aware food recommender</strong> built specifically for students at
        Shoolini University, Solan. It combines <strong>affective computing</strong>, <strong>vector semantic search</strong>,
        and <strong>real local menu data</strong> to recommend food that actually matches how you feel.</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="about-grid">
        <div class="about-card">
            <h3>🧠 Why This Matters</h3>
            <ul>
                <li>People feel confused about what to eat</li>
                <li>Mood directly affects food preferences</li>
                <li>Decision fatigue is real and exhausting</li>
                <li>This app makes the decision for you</li>
                <li>Comfort food helps with anxiety and stress</li>
            </ul>
        </div>
        <div class="about-card">
            <h3>🔬 The Technology</h3>
            <ul>
                <li>ChromaDB vector database</li>
                <li>Sentence-transformers embeddings</li>
                <li>Google Gemini API for natural language</li>
                <li>RAG (Retrieval-Augmented Generation)</li>
                <li>Python rule-based emotion engine</li>
                <li>Streamlit frontend</li>
            </ul>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("### 🌿 Wellness Tips")
    st.markdown("""
    <div class="wellness-grid">
        <div class="wellness-card" style="background:#FFE4CC;border-left:4px solid #E8732A">
            <h4>😰 If stressed</h4>
            <ul><li>Drink warm tea or soup</li><li>Eat light comfort food</li><li>Avoid skipping meals</li></ul>
        </div>
        <div class="wellness-card" style="background:#E8EAFF;border-left:4px solid #9B8EC4">
            <h4>😴 If tired</h4>
            <ul><li>Choose easy-to-digest meals</li><li>Avoid heavy fried food</li><li>Stay hydrated</li></ul>
        </div>
        <div class="wellness-card" style="background:#D4F5E9;border-left:4px solid #5BAF6E">
            <h4>😊 If happy</h4>
            <ul><li>Try new cuisines</li><li>Eat balanced meals</li><li>Share food with friends</li></ul>
        </div>
        <div class="wellness-card" style="background:#FFF0E0;border-left:4px solid #F4A646">
            <h4>😟 If anxious</h4>
            <ul><li>Stick to familiar food</li><li>Avoid too much caffeine</li><li>Warm food calms the nerves</li></ul>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
        <h3 style="text-align:center;margin-bottom:24px;">👥 Built by</h3>
        <div class="team-grid">
            <div class="team-card" style="background:#FFE4CC">
                <div class="team-init">D</div>
                <div class="team-name">Divya Ohri</div>
                <div class="team-reg">GF202453419</div>
                <div class="team-role">🔧 Backend & GenAI</div>
            </div>
            <div class="team-card" style="background:#D4F5E9">
                <div class="team-init">A</div>
                <div class="team-name">Aishwarya Rana</div>
                <div class="team-reg">GF202453090</div>
                <div class="team-role">🗄️ RAG & Vector DB</div>
            </div>
            <div class="team-card" style="background:#E8EAFF">
                <div class="team-init">D</div>
                <div class="team-name">Diya</div>
                <div class="team-reg">GF202460495</div>
                <div class="team-role">🎨 Frontend & UI</div>
            </div>
            <div class="team-card" style="background:#FFF3C4">
                <div class="team-init">K</div>
                <div class="team-name">Kashish</div>
                <div class="team-reg">GF202462554</div>
                <div class="team-role">📋 Testing & Docs</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br><center><small style='color:#8A7A72'>Made with ❤️ at Yogananda School of AI, Shoolini University · CSU2217</small></center>", unsafe_allow_html=True)