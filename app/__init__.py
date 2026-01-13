from flask import Flask
from dotenv import load_dotenv

from .config import get_config
from .extensions import db, migrate

from .web import web_bp
from .api import register_api_blueprints


def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config.from_object(get_config())

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(web_bp)
    register_api_blueprints(app)

    return app