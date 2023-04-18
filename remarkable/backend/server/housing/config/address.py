"""Configuration for address endpoints"""

from flask_restx.reqparse import RequestParser

owner_parser = RequestParser()
owner_parser.add_argument(
    "id", required=True, action="store", help="UUID of owner", nullable=False
)
owner_args = owner_parser.parse_args()

neighborhood_parser = RequestParser()
neighborhood_parser.add_argument(
    "id", required=True, action="store", help="UUID of neighborhood", nullable=False
)
neighborhood_args = neighborhood_parser.parse_args()

address_by_id_parser = RequestParser()
address_by_id_parser.add_argument(
    "id", required=True, action="store", help="UUID of address", nullable=False
)
address_by_id_args = address_by_id_parser.parse_args()
