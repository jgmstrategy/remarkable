"""Models for units listed for sale"""

from flask_restx import Namespace
from flask_restx.fields import Boolean, DateTime, Float, Nested, String

api = Namespace("sale", "Sale price related operations")

listing = api.model(
    "Estate Listing",
    {
        "id": String(name="Listing ID", description="UUID of a listing", required=True),
        "address": String(
            name="Address ID", description="UUID of associated address", required=True
        ),
        "price": Float(
            name="Price", description="Price update or object", required=True
        ),
        "type_flags": Nested(
            api.model(
                "Estate Flags",
                {
                    "foreclosure": Boolean(
                        default=False,
                        title="Foreclosure",
                        description="Is foreclosure or foreclosed",
                        required=False,
                    ),
                    "auction": Boolean(
                        default=True,
                        title="Auction",
                        description="Is an auction",
                        required=False,
                    ),
                    "bid": Boolean(
                        default=False,
                        title="Bid",
                        description="Price entry is a bid",
                        required=False,
                    ),
                },
            ),
            title="Listing Type Flags",
            allow_null=False,
            skip_none=False,
        ),
        "ts": DateTime(title="Timestamp", description="Price timestamp", required=True),
    },
    strict=True,
)
