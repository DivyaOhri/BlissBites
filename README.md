# 🍜 BlissBites — Eat What You Feel

**Smart Food Recommender with Emotion-Aware Analysis**
Yogananda School of AI · Shoolini University · CSU2217

---

## 🎯 The Problem

Students at Shoolini University often struggle with:
- **Decision fatigue** — Can't decide what to eat after long classes
- **Mood-food disconnect** — Eating without considering how it affects their energy and emotions
- **Budget constraints** — Need affordable options that satisfy cravings
- **Lack of personalization** — Generic food apps don't consider emotional state

## 💡 Our Solution

**BlissBites** is an emotion-aware food recommendation system that:
1. Understands how you're feeling (mood, stress, energy levels)
2. Maps your emotional state to foods that actually help
3. Recommends from real local restaurant menus near campus
4. Provides AI-powered explanations for why certain foods match your mood

## 🎯 Target Audience

- **Primary:** University students at Shoolini University
- **Secondary:** Young professionals in the Solan area
- **Tertiary:** Anyone interested in mindful eating based on emotional state

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Emotion Detection** | Analyzes mood, stress level (1-10), and energy (0-100) to understand user state |
| **Smart Food Mapping** | Maps emotional profiles to food categories using rule-based logic |
| **Vector Search** | ChromaDB semantic search finds similar foods based on tags and descriptions |
| **AI Explanations** | Google Gemini generates personalized wellness tips and food science |
| **Local Data** | 1,527 real food items from restaurants near Shoolini University |
| **Budget Awareness** | Filters recommendations by price range |
| **Dietary Preferences** | Supports vegetarian, vegan, non-vegetarian preferences |
| **History Tracking** | Saves mood and food history for personalized insights |
| **Interactive Games** | Food-themed games (Bingo, Word Search, Memory, Tic-Tac-Toe) for engagement |

---

## 📊 Data & Scale

- **Food Database:** 1,527 items from 10+ local restaurants
- **Vector Embeddings:** all-MiniLM-L6-v2 (384 dimensions)
- **Collections:** Foods, Profiles, Feedback, Mood History
- **Storage:** ChromaDB (vector) + JSON (structured data)

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
python backend/run.py
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
│   ├── run.py                  ← Flask server (main entry point) ✅
│   ├── app.py                  ← Streamlit alternative frontend
│   ├── ai_services.py          ← Google Gemini AI integration
│   ├── data_storage.py         ← Logic for handling JSON persistence
│   ├── food_data.py            ← 1,527 food items with tags/prices
│   ├── food_retrieval.py       ← Vector search + hybrid retrieval
│   ├── vector_store.py         ← ChromaDB multi-collection management
│   ├── chroma_data/            ← Persistent ChromaDB vector storage
│   ├── data/                   ← User data (JSON files)
│   │   ├── feedback.json       ← Food rating feedback
│   │   ├── history.json        ← Mood & food history
│   │   └── profiles.json       ← User preferences
│   └── src/
│       ├── emotion_engine/     ← Core mood detection pipeline
│       │   ├── food_intent_logic.py
│       │   ├── output_builder.py
│       │   ├── pipeline.py
│       │   ├── questionnaire.py
│       │   └── scoring.py
│       └── main.py             ← Standalone pipeline runner
│
├── tests/                      ← Unit tests
│   ├── test_food_intent.py
│   ├── test_output_builder.py
│   ├── test_pipeline.py
│   ├── test_questionnaire.py
│   └── test_scoring.py
│
├── .env                        ← API keys (GEMINI_API_KEY)
├── .gitignore                  ← Excludes .env, __pycache__, .pytest_cache
├── README.md
├── requirements.txt            ← All dependencies
└── test_backend.py             ← Root-level backend tests
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
| Frontend | HTML, CSS, Vanilla JavaScript |
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
|--------|----------|-------------|
| GET | `/` | Serves the `app.html` frontend |
| POST | `/api/analyse` | Accepts mood/stress/energy/budget, returns food recommendations + AI response |
| POST | `/api/profile/save` | Saves user profile (name, dietary, cuisine, budget) |
| GET | `/api/profile/<user_id>` | Retrieves user profile |
| POST | `/api/history` | Saves mood/food history entry |
| GET | `/api/history/<user_id>` | Retrieves user's mood and food history |
| POST | `/api/feedback` | Saves user feedback for recommendations |
| GET | `/api/feedback/<user_id>` | Retrieves user's feedback history |
| GET | `/api/stats/<user_id>` | Gets user statistics (mood trends, popular foods) |

---

## 💰 Business Model & Monetization

### Current State
- Free-to-use prototype for university students
- No revenue generation — focus on user acquisition and feedback

### Future Revenue Streams (Scalability)
| Stream | Description |
|--------|-------------|
| **Restaurant Partnerships** | Commission from local restaurants for featured recommendations |
| **Premium Features** | Advanced analytics, personalized meal plans, subscription model |
| **Campus Sponsorships** | Sponsored listings by food chains targeting students |
| **Data Insights** | Anonymized mood-food trend data for market research |
| **Delivery Integration** | Partner with Swiggy/Zomato for direct ordering |

---

## 🏆 Competitive Advantage

| Aspect | BlissBites | Competitors |
|--------|------------|-------------|
| **Emotion-Aware** | ✅ Yes — mood, stress, energy mapping | ❌ No |
| **Local Data** | ✅ 1,527 real menu items | ❌ Generic national data |
| **Budget-Aware** | ✅ Price filtering | ❌ Limited |
| **AI Explanations** | ✅ Gemini-powered wellness tips | ❌ None |
| **Free to Use** | ✅ Yes | ❌ Usually paid |
| **Offline Fallback** | ✅ Local retrieval if server down | ❌ No |

---

## 🔮 Future Scope

### Short-term (3-6 months)
- [ ] Add user authentication (login/signup)
- [ ] Push notifications for meal reminders
- [ ] Integration with food delivery apps
- [ ] Social features (share recommendations)

### Long-term (6-12 months)
- [ ] Mobile app (iOS/Android)
- [ ] Multi-language support (Hindi, English)
- [ ] Expand to other universities
- [ ] AI-powered nutritional analysis
- [ ] Partner with campus mess/cafeteria

---

## 👥 Team & Credits

- **Project Lead:** Yogananda School of AI, Shoolini University
- **Course:** CSU2217 — AI/ML Capstone Project
- **Mentor:** Dr. [Name]
- **Tech Support:** ChromaDB, Google Gemini, Sentence Transformers

---

*Made with ❤️ at Yogananda School of AI, Shoolini University · CSU2217*