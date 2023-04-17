from flask import Flask


def create_app(config_obj, test_config=None) -> Flask:
    app = Flask(__name__)

    return app
