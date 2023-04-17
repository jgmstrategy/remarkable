from flask import Blueprint, Flask
from flask_restx import Api

# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

# from .config import config_by_name

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="remarkable backend",
    version="1.0",
    description="remarkable backend",
)

# api.add_namespace(user_ns, path="/user")


# db = SQLAlchemy()
# flask_bcrypt = Bcrypt()


def create_app(config_name) -> Flask:
    app = Flask(__name__)
    # app.config.from_object(config_by_name[config_name])
    # db.init_app(app)
    # flask_bcrypt.init_app(app)

    return app
