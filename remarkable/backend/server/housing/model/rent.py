"""Models for units listed for rent"""

from flask_restx import Namespace
from flask_restx.fields import DateTime, Float, String, Integer, Nested, Boolean

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
        "contract_length": Integer(
            default=12,
            name="Contract Length",
            description="Length of contract in months",
            required=True,
        ),
        "ts": DateTime(title="Timestamp", description="Price timestamp", required=True),
        "discount": Float(
            default=0,
            name="Discount",
            description="Total value of discount, if contract is followed",
            required=False,
        ),
        "utilities": Nested(
            {
                "electricity": Boolean(default=False, required=False),
                "water": Boolean(default=False, required=False),
                "trash": Boolean(default=False, required=False),
                "sewage": Boolean(default=False, required=False),
                "gas": Boolean(default=False, required=False),
            },
            title="Included Utilities",
            description="Utilities included for free",
            required=True,
            allow_null=False,
            skip_none=False,
        ),
    },
    strict=True,
)
