from flask import Flask
from .health import health_bp


def register_api_blueprints(app: Flask) -> None:
    app.register_blueprint(health_bp, url_prefix='/api')