"""Configuration for rent endpoints"""

from flask_restx.reqparse import RequestParser

entry_params = RequestParser()
entry_params.add_argument(
    "id", required=True, action="store", help="UUID of entry", nullable=False
)
