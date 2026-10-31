from .main import main_bp
from .story import story_bp
from .explore import explore_bp
from .map import map_bp


def create_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(story_bp)
    app.register_blueprint(explore_bp)
    app.register_blueprint(map_bp)