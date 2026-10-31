import os
import urllib.parse

import google.generativeai as genai
import requests

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    model_name=os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash")
)

REQUEST_TIMEOUT = 10
WIKI_HEADERS = {
    "User-Agent": "TimeTales/1.0 (https://github.com/divyasrees16/TimeTales)"
}


def get_gemini_story(era, language="English"):
    prompt = f"""
    You are a poetic historian fluent in {language}.
    Write a vivid, immersive walkthrough of a day in {era}.
    Include:
    - Descriptions of people, places, and daily life
    - Mention 2-3 archaeological facts or ancient landmarks
    - Keep it poetic and storytelling style

    Write the entire story only in {language}.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating story: {str(e)}"


def _fetch_wiki_summary(title):
    """Return the Wikipedia summary JSON for an exact page title, or None."""
    url = (
        "https://en.wikipedia.org/api/rest_v1/page/summary/"
        + urllib.parse.quote(title.replace(" ", "_"), safe="")
    )
    try:
        response = requests.get(url, headers=WIKI_HEADERS, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return response.json()
    except (requests.RequestException, ValueError):
        pass
    return None


def _search_wiki_title(query):
    """Return the best-matching Wikipedia page title for a free-text query."""
    try:
        response = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "srlimit": 1,
                "format": "json",
            },
            headers=WIKI_HEADERS,
            timeout=REQUEST_TIMEOUT,
        )
        results = response.json().get("query", {}).get("search", [])
        if results:
            return results[0]["title"]
    except (requests.RequestException, ValueError, KeyError):
        pass
    return None


def get_wikipedia_summary_and_image(era):
    """Return (summary, image_url, page_url). image_url/page_url may be None."""
    cleaned = era.strip().replace("Tell me about", "").strip()

    data = _fetch_wiki_summary(cleaned)
    if data is None:
        matched_title = _search_wiki_title(cleaned)
        if matched_title:
            data = _fetch_wiki_summary(matched_title)

    if data is None:
        return f"No Wikipedia page found for '{cleaned}'.", None, None

    summary = data.get("extract") or f"No summary found for '{cleaned}'."
    image_url = (data.get("thumbnail") or {}).get("source")
    page_url = (data.get("content_urls") or {}).get("desktop", {}).get("page")
    return summary, image_url, page_url