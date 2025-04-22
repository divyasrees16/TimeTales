import os
import requests
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-002")

def get_gemini_story(era):
    prompt = f"""
    You are a poetic historian. Write a vivid, immersive walkthrough of a day in {era}.
    Include:
    - Descriptions of people, places, and daily life
    - Mention 2-3 archaeological facts or ancient landmarks
    - Keep it poetic and storytelling style
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating story: {str(e)}"

def get_unsplash_image(query):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={os.getenv('UNSPLASH_ACCESS_KEY')}"
    response = requests.get(url)
    data = response.json()
    if data.get("results"):
        return data["results"][0]["urls"]["regular"]
    return None
