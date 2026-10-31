# ⏳ TimeTales – Step Into History with AI Narratives

**TimeTales** is an interactive platform that generates immersive, poetic stories about historical eras in multiple languages. By combining Generative AI with real archaeological facts and visuals, users can explore the past like never before.

## 🌟 Features

- 🔮 **AI-Powered Historical Narratives** – Generates vivid stories about ancient civilizations, battles, and landmarks.
- 🌍 **Multilingual Support** – Choose your preferred language to read the story in (English, Tamil, Hindi or Telugu).
- 🧭 **Interactive Timeline & Map** – Browse a visual timeline of eras and explore historical landmarks on a map with informative popups.
- 📚 **Wikipedia Integration** – Fetches accurate summaries, images and links for historical events or places.
- 🎨 **Beautiful UI** – Clean, responsive design with a poetic feel using HTML, CSS, and Leaflet.js.

## 🛠️ Tech Stack

- **Backend:** Python, Flask (blueprints)
- **AI Model:** Gemini 1.5 via Google Generative AI
- **NLP:** Prompt-based multilingual text generation
- **APIs Used:**
  - Wikipedia REST API (for summaries and images)
  - Leaflet.js with OpenStreetMap tiles (for interactive maps)
- **Frontend:** HTML, CSS, Jinja2 Templates

## 📁 Project Structure

```
TimeTales/
├── app.py                # App factory and entry point
├── requirements.txt      # Python dependencies
├── .env.example          # Template for required environment variables
├── routes/               # Flask blueprints
│   ├── __init__.py       # Registers all blueprints
│   ├── main.py           # Home page (era + language form)
│   ├── story.py          # Story page
│   ├── explore.py        # Timeline page
│   └── map.py            # Landmarks map page
├── utils/
│   └── ai_helpers.py     # Gemini story generation + Wikipedia lookup
├── templates/            # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── story.html
│   ├── explore.html
│   └── map.html
└── static/
    └── css/style.css     # Site styles
```

## 🚀 Get Started

### 1. Clone the repository

```bash
git clone https://github.com/divyasrees16/TimeTales.git
cd TimeTales
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your API key

Copy `.env.example` to `.env` and add your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get a key at [Google AI Studio](https://aistudio.google.com/app/apikey). 

Optionally, set `GEMINI_MODEL` in `.env` to use a different Gemini model.

### 4. Run the app

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

