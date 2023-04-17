"""Models for units listed for rent"""

from flask_restx import Namespace
from flask_restx.fields import Float, String

api = Namespace("rent", "Rent related operations")

entry = api.model(
    "entry",
    {
        "id": String(
            name="Entry ID", description="UUID of a price entry", required=True
        ),
        "address": String(
            name="Address ID", description="UUID of associated address", required=True
        ),
        "price": Float(
            name="Price", description="Price update or object", required=True
        ),
    },
    strict=True,
)
