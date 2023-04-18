"""Configuration for address endpoints"""

from flask_restx.reqparse import RequestParser

owner_params = RequestParser()
owner_params.add_argument(
    "id", required=True, action="store", help="UUID of owner", nullable=False
)

neighborhood_params = RequestParser()
neighborhood_params.add_argument(
    "id", required=True, action="store", help="UUID of neighborhood", nullable=False
)

address_params = RequestParser()
address_params.add_argument(
    "id", required=True, action="store", help="UUID of address", nullable=False
)
