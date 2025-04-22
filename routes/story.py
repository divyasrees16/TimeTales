from flask import Blueprint, render_template, request
from utils.ai_helpers import get_gemini_story, get_unsplash_image

story_bp = Blueprint('story', __name__)

@story_bp.route("/story")
def view_story():
    era = request.args.get("era")
    if not era:
        return "Era not provided", 400
    story = get_gemini_story(era)
    image_url = get_unsplash_image(era)
    return render_template("story.html", story=story, image_url=image_url, era=era)
