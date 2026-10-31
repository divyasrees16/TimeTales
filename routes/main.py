from flask import Blueprint, render_template, request, redirect, url_for
from .languages import ALLOWED_LANGUAGES

main_bp = Blueprint('main', __name__)


@main_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        era = request.form.get("era", "").strip()
        language = request.form.get("language", "English")
        if era:
            return redirect(url_for('story.view_story', era=era, language=language))
    return render_template("index.html", allowed_languages=ALLOWED_LANGUAGES)