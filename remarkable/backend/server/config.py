"""Configuration for backend"""

from os import path

BASE_DIR = path.abspath(path.dirname(__file__))
FLASK_CONFIG = {
    "SQLALCHEMY_DATABASE_URI": f"sqlite:///{path.join(BASE_DIR, 'database.db')}",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
}
