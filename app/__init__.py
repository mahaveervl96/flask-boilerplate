from flask import Flask
from dotenv import load_dotenv

from .web import web_bp


def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.register_blueprint(web_bp)

    return app