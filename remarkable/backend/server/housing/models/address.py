"""Models for local addressing"""

from flask_restx import Namespace
from flask_restx.fields import Boolean, Float, Integer, List, Nested, String
from sqlalchemy.orm import Mapped

from remarkable.backend.server.models import Base, db

api = Namespace("address", description="Location related operations")

owner = api.model(
    "Owner",
    {
        "id": String(
            name="Name ID",
            description="UUID of a owner name",
            required=True,
            example="00000000-0000-0000-0000-000000000000",
        ),
        "name": String(
            name="Name",
            description="Name",
            required=True,
            example="Regents of California",
        ),
    },
)


# pylint: disable=too-few-public-methods
class Owner(Base):
    """Owners table"""

    __tablename__ = "owners"

    name: Mapped[str] = db.Column(db.String, nullable=False)


neighborhood = api.model(
    "Neighborhood",
    {
        "id": String(
            title="Neighborhood ID",
            description="UUID of neighborhood",
            required=True,
            example="00000000-0000-0000-0000-000000000000",
        ),
        "name": String(
            title="Neighborhood name",
            description="Name of the neighborhood",
            required=False,
            example="La Jolla Farms",
        ),
        "gated": Boolean(
            default=False,
            title="Gated Community",
            description="Whether or not the community is gated",
            required=True,
            example=False,
        ),
        "hoa": Boolean(
            default=False,
            title="HOA",
            description="Whether or not the community has HOA",
            required=True,
            example=False,
        ),
    },
    strict=True,
)


# pylint: disable=too-few-public-methods
class Neighborhood(Base):
    """Neighborhood table"""

    __tablename__ = "neighborhoods"

    name: Mapped[str] = db.Column(db.String, nullable=True)
    gated: Mapped[bool] = db.Column(db.Boolean, nullable=False, server_default=False)
    hoa: Mapped[bool] = db.Column(db.Boolean, nullable=False, server_default=False)


address = api.model(
    "Address",
    {
        "id": String(
            title="Location ID",
            description="UUID of location",
            required=True,
            example="00000000-0000-0000-0000-000000000000",
        ),
        "mls": String(
            title="MLS Number",
            description="Real estate listing number",
            required=False,
            example="0000000",
        ),
        "name": String(
            title="Name",
            description="Friendly name of address",
            required=False,
            example="Audrey Geisel University House",
        ),
        "owner": String(
            name="Owner ID",
            description="UUID of owner",
            required=False,
            example="00000000-0000-0000-0000-000000000000",
        ),
        "neighborhood": String(
            title="Neighborhood",
            description="UUID of neighborhood",
            required=False,
            example="00000000-0000-0000-0000-000000000000",
        ),
        "number": String(
            title="House Number",
            description="Number on address",
            required=True,
            example="9630",
        ),
        "street": String(
            title="Street",
            description="Street address",
            required=True,
            example="La Jolla Farms Rd",
        ),
        "zip": String(title="Zip Code", required=True, example="92037"),
        "county": String(title="County", required=False, example="San Diego"),
        "city": String(title="City", required=True, example="La Jolla"),
        "state": String(title="State", required=True, example="CA"),
        "country": String(title="Country", required=True, example="USA"),
        "tra": String(title="Tax Rate Area Code", required=False, example="3487"),
        "built_year": Integer(
            title="Year Built",
            description="Year the address was built",
            required=False,
            example=1952,
        ),
        "units": Integer(
            default=1,
            title="Units",
            description="Number of units at this address",
            required=True,
            example=1,
        ),
        "beds": Integer(
            title="Bedrooms",
            description="Number of bedrooms, if single unit",
            required=False,
            example=17,
        ),
        "baths": Float(
            title="Bathrooms",
            description="Number of bathrooms, if single unit",
            required=False,
            example=17.5,
        ),
        "floor_space": Integer(
            title="Floor Space",
            description="sq.ft. of floor space, if single unit",
            required=False,
            example=26674,
        ),
        "floors": Integer(
            default=1,
            title="Stories",
            description="Number of stories",
            required=True,
            example=1,
        ),
        "pool": Nested(
            api.model(
                "Pool Data",
                {
                    "has_pool": Boolean(
                        default=False,
                        title="Pool",
                        description="Property has a private pool",
                        required=True,
                        example=True,
                    ),
                    "pool_size": Integer(
                        title="Pool Size",
                        description="Pool area",
                        required=False,
                        example=70,
                    ),
                },
            ),
            title="Pool Data",
            allow_null=False,
            skip_none=False,
        ),
        "parking": Nested(
            api.model(
                "Parking Data",
                {
                    "garage": Integer(
                        default=0,
                        title="Garage Spots",
                        description="Number of spots in a garage",
                        required=True,
                        example=10,
                    ),
                    "covered": Integer(
                        default=0,
                        title="Covered Spots",
                        description="Number of top-covered spots",
                        required=True,
                        example=0,
                    ),
                    "uncovered": Integer(
                        default=0,
                        title="Uncovered Spots",
                        description="Number of uncovered, non-street spots",
                        required=True,
                        example=22,
                    ),
                },
            ),
            allow_null=False,
            skip_none=False,
            required=True,
        ),
        "parent": String(
            title="Parent Address",
            description="Parent UUID, if it is part of another address",
            required=False,
            example="00000000-0000-0000-0000-000000000000",
        ),
        "children": List(
            String(
                title="Children Address",
                description="Children UUID, if it has subdivided units",
                required=False,
                example="00000000-0000-0000-0000-000000000000",
            ),
            required=False,
        ),
    },
    strict=True,
)


# pylint: disable=too-few-public-methods
class Address(Base):
    """Addresses table"""

    __tablename__ = "addresses"

    mls: Mapped[str] = db.Column(db.String, nullable=True)
    name: Mapped[str] = db.Column(db.String, nullable=True)
    owner: Mapped[str] = db.Column(db.String, nullable=True)
    neighborhood: Mapped[str] = db.Column(db.String, nullable=True)
    number: Mapped[str] = db.Column(db.String)
    street: Mapped[str] = db.Column(db.String)
    zip: Mapped[str] = db.Column(db.String)
    county: Mapped[str] = db.Column(db.String)
    city: Mapped[str] = db.Column(db.String)
    state: Mapped[str] = db.Column(db.String)
    country: Mapped[str] = db.Column(db.String, nullable=True)
    tra: Mapped[str] = db.Column(db.String, nullable=True)
    built_year: Mapped[int] = db.Column(db.Integer, nullable=True)
    units: Mapped[int] = db.Column(db.Integer, server_default=1)
    beds: Mapped[int] = db.Column(db.Integer, nullable=True)
    baths: Mapped[float] = db.Column(db.Float, nullable=True)
    floor_space: Mapped[int] = db.Column(db.Integer, nullable=True)
    floors: Mapped[int] = db.Column(db.Integer, server_default=1)
    has_pool: Mapped[bool] = db.Column(db.Boolean, server_default=False)
    pool_size: Mapped[int] = db.Column(db.Integer, nullable=True)
    garage_spaces: Mapped[int] = db.Column(db.Integer, server_default=0)
    covered_spaces: Mapped[int] = db.Column(db.Integer, server_default=0)
    uncovered_spaces: Mapped[int] = db.Column(db.Integer, server_default=0)
    parent: Mapped[str] = db.Column(db.String, nullable=True)
    children: Mapped[str] = db.Column(db.String, nullable=True)
