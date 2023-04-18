"""Models for units listed for sale"""

import datetime

from flask_restx import Namespace
from flask_restx.fields import Boolean, DateTime, Float, Nested, String
from sqlalchemy.orm import Mapped

from remarkable.backend.server.models import Base, db

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


# pylint: disable=too-few-public-methods
class EstateListing(Base):
    """Real estate listing table"""

    __tablename__ = "estate_listings"

    address: Mapped[str] = db.Column(db.String)
    price: Mapped[float] = db.Column(db.Float)
    foreclosure: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    auction: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    bid: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    ts: Mapped[datetime.datetime] = db.Column(
        db.DateTime, default=db.func.current_timestamp()
    )
