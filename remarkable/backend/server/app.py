"""Creates the Flask server"""

from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from remarkable.backend.server.config import FLASK_CONFIG
from remarkable.backend.server.controller import api
from remarkable.backend.server.models import db


def create_app(app_api: Api) -> Flask:
    """Create the Flask object"""
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)  # type: ignore

    for key, value in FLASK_CONFIG.items():
        app.config[key] = value

    app_api.init_app(app)
    db.init_app(app)

    return app


flask_app = create_app(api)

if __name__ == "__main__":
    flask_app.run()
