from flask import Blueprint, render_template, request
from utils.ai_helpers import get_gemini_story, get_wikipedia_summary_and_image
from .languages import ALLOWED_LANGUAGES

story_bp = Blueprint('story', __name__)


@story_bp.route("/story")
def view_story():
    era = request.args.get("era", "").strip()
    language = request.args.get("language", "English")

    if not era:
        return "Era not provided", 400
    if language not in ALLOWED_LANGUAGES:
        language = "English"

    story = get_gemini_story(era, language)
    summary, image_url, wiki_url = get_wikipedia_summary_and_image(era)

    return render_template(
        "story.html",
        story=story,
        era=era,
        language=language,
        summary=summary,
        image_url=image_url,
        wiki_url=wiki_url,
    )