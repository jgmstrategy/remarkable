"""Models for units listed for rent"""

import datetime

from flask_restx import Namespace
from flask_restx.fields import Boolean, DateTime, Float, Integer, Nested, String
from sqlalchemy.orm import Mapped

from remarkable.backend.server.models import Base, db

api = Namespace("rent", "Rent related operations")

entry = api.model(
    "Rent Entry",
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
            api.model(
                "utilities",
                {
                    "electricity": Boolean(default=False, required=False),
                    "water": Boolean(default=False, required=False),
                    "trash": Boolean(default=False, required=False),
                    "sewage": Boolean(default=False, required=False),
                    "gas": Boolean(default=False, required=False),
                },
            ),
            title="Included Utilities",
            description="Utilities included for free",
            required=True,
            allow_null=False,
            skip_none=False,
        ),
    },
    strict=True,
)


# pylint: disable=too-few-public-methods
class RentEntry(Base):
    """Rent entry table"""

    __tablename__ = "rent_entries"

    address: Mapped[str] = db.Column(db.String)
    price: Mapped[float] = db.Column(db.Float)
    contract_length: Mapped[int] = db.Column(db.Integer, nullable=True, default=12)
    ts: Mapped[datetime.datetime] = db.Column(
        db.DateTime, default=db.func.current_timestamp()
    )
    discount: Mapped[float] = db.Column(db.Float, nullable=True, default=0)
    electricity: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    water: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    trash: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    sewage: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
    gas: Mapped[bool] = db.Column(db.Boolean, nullable=True, default=False)
