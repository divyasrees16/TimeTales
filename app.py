from flask import Flask
from routes import create_routes
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    create_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
