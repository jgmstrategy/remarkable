"""Configuration for sale endpoints"""

from flask_restx.reqparse import RequestParser

listing_params = RequestParser()
listing_params.add_argument(
    "id", required=True, action="store", help="UUID of sale listing", nullable=False
)
