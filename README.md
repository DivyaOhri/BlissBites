# 🍜 BlissBites — Eat What You Feel

**Smart Food Recommender with Emotion-Aware Analysis**
Yogananda School of AI · Shoolini University · CSU2217

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/YourUsername/BlissBites.git
cd BlissBites
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Flask server
```bash
python backend/app.py
```

### 5. Open in your browser
```
http://localhost:5000
```

The full app will load directly in your browser — no Streamlit needed.

---

## 📁 File Structure

```
BlissBites/
├── frontend/
│   └── app.html                ← Full HTML frontend (all pages + CSS + JS)
│
├── backend/
│   ├── app.py                  ← Flask server (main entry point)
│   ├── ai_services.py          ← Google Gemini AI integration
│   ├── data_storage.py         ← Logic for handling JSON persistence
│   ├── food_data.py            ← Raw restaurant/food data definitions
│   ├── food_retrieval.py       ← Search logic for recommendations
│   ├── run.py                  ← Alternative startup script
│   ├── vector_store.py         ← ChromaDB configuration and indexing
│   ├── chroma_data/            ← Persistent ChromaDB vector collections
│   ├── data/                   ← Local storage for user interactions
│   │   ├── feedback.json
│   │   ├── history.json
│   │   └── profiles.json
│   ├── moodbite_db/            ← Core database storage for mood mappings
│   └── src/
│       ├── emotion_engine/     ← Core mood + scoring pipeline
│       │   ├── food_intent_logic.py
│       │   ├── output_builder.py
│       │   ├── pipeline.py
│       │   ├── questionnaire.py
│       │   └── scoring.py
│       └── main.py             ← Standalone pipeline runner
│
├── tests/                      ← Unit and integration tests
│   ├── test_food_intent.py
│   ├── test_output_builder.py
│   ├── test_pipeline.py
│   ├── test_questionnaire.py
│   └── test_scoring.py
│
├── .env                        ← Environment variables (Local only)
├── .gitignore                  ← Prevents pushing .env and __pycache__
├── README.md
├── requirements.txt            ← All dependencies
└── test_backend.py             ← Root-level backend testing script
```

---

## 🗺️ App Pages

| Page | Purpose |
|---|---|
| 🏠 Home | Welcome screen with features, stats, and how it works |
| 😊 Mood Check | Mood selector, stress/energy sliders, vent box, budget & cuisine preferences |
| 💡 Mood Insights | Detected mood card, energy/stress meters, AI explanation, food tags, wellness tip |
| 💰 Budget Insights | Budget vs best match, savings display, price comparison bars |
| 🍽️ Food Details | Detailed food cards with descriptions, tags, and food science explanation |
| 👤 Profile | Save name, dietary type, cuisine preference, and budget |
| ✨ Results | Top 3 food recommendations with rankings, summary bar, and encouragement |
| 🎮 Playroom | 4 food-themed games to play while waiting for your order |
| 🍿 CineMatch | Movie recommendations based on genre, language, and vibe |
| 💬 Feedback | Rate your experience and share suggestions for improvement |
| 📖 About | Project info, tech stack, and wellness tips |

---

## 🔧 How the Pipeline Works

```
User fills Mood Check (mood + stress + energy + budget + vent box)
        ↓
Flask API (/api/analyse) receives the input
        ↓
Emotion Engine: scoring → mood detection → energy classification
        ↓
Food Intent Mapping: mood + energy → food type + keywords
        ↓
Vector Retrieval: ChromaDB similarity search over local restaurant data
        ↓
AI Explanation: Google Gemini generates a friendly response
        ↓
JSON response sent back to app.html
        ↓
Results rendered dynamically in the browser
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3(Grid/Flexbox), Vanilla JavaScript |
| Backend | Python Flask |
| Emotion Engine | Python rule-based logic |
| Vector Search | ChromaDB + sentence-transformers |
| AI Responses | Google Gemini 2.5 Flash |
| Embeddings | all-MiniLM-L6-v2 |
| Language | Python 3.10+ |

---

## 🎮 Games in the Playroom

| Game | Description |
|---|---|
| 🍱 Food Bingo | Roll food items and mark your 4×4 bingo card |
| 🔍 Food Word Search | Find hidden food words in an 8×8 letter grid |
| 🧠 Sensory Memory Match | Flip and match food emoji pairs |
| 🍔 Food Tic-Tac-Toe | Play against an unbeatable Minimax AI |

---

## 🧪 Running Tests
```bash
python -m pytest -q
```

Or run the standalone backend demo:
```bash
python backend/src/main.py
```

---

## 🔑 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the `app.html` frontend |
| POST | `/api/analyse` | Accepts mood/stress/energy/budget, returns food recommendations + AI response |

---

*Made with ❤️ at Yogananda School of AI, Shoolini University · CSU2217*
