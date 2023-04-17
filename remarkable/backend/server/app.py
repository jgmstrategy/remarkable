"""Creates the Flask server"""

from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from remarkable.backend.server.controller import api


def create_app(app_api: Api) -> Flask:
    """Create the Flask object"""
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)  # type: ignore

    app_api.init_app(app)
    # db.init_app(app)
    # flask_bcrypt.init_app(app)

    return app


if __name__ == "__main__":
    flask_app = create_app(api)
    flask_app.run()
