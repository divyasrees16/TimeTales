from flask import Blueprint, render_template, request, redirect, url_for
from utils.ai_helpers import get_gemini_story, get_unsplash_image

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        era = request.form["era"]
        return redirect(url_for('story.view_story', era=era))
    return render_template("index.html")
