from flask import Blueprint, render_template

explore_bp = Blueprint('explore', __name__)

@explore_bp.route("/explore")
def explore():
    return render_template("explore.html")  # Add timeline UI later
