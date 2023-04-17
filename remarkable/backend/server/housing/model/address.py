"""Models for local addressing"""

from flask_restx import Namespace
from flask_restx.fields import Boolean, Float, Integer, List, Nested, String

api = Namespace("address", description="Location related operations")

owner = api.model(
    "owner",
    {
        "id": String(name="Name ID", description="UUID of a owner name", required=True),
        "name": String(name="Name", description="Name", required=True),
    },
)

neighborhood = api.model(
    "Neighborhood",
    {
        "id": String(
            title="Neighborhood ID", description="UUID of neighborhood", required=True
        ),
        "gated": Boolean(
            default=False,
            title="Gated Community",
            description="Whether or not the community is gated",
            required=True,
        ),
        "hoa": Boolean(
            default=False,
            title="HOA",
            description="Whether or not the community has HOA",
            required=True,
        ),
    },
    strict=True,
)

address = api.model(
    "Address",
    {
        "id": String(
            title="Location ID", description="UUID of location", required=True
        ),
        "mls": String(
            title="MLS Number", description="Real estate listing number", required=False
        ),
        "name": String(
            title="Name", description="Friendly name of community", required=False
        ),
        "owner": String(name="Owner ID", description="UUID of owner", required=False),
        "community": String(
            title="Community", description="UUID of community", required=False
        ),
        "number": String(
            title="House Number", description="Number on address", required=True
        ),
        "street": String(title="Street", description="Street address", required=True),
        "zip": String(title="Zip Code", required=True),
        "county": String(title="County", required=True),
        "tra": String(title="Tax Rate Area Code", required=False),
        "built_year": Integer(
            title="Year Built", description="Year the address was built", required=False
        ),
        "units": Integer(
            default=1,
            title="Units",
            description="Number of units at this address",
            required=True,
        ),
        "beds": Integer(
            title="Bedrooms",
            description="Number of bedrooms, if single unit",
            required=False,
        ),
        "baths": Float(
            title="Bathrooms",
            description="Number of bathrooms, if single unit",
            required=False,
        ),
        "floor_space": Integer(
            title="Floor Space",
            description="sq.ft. of floor space, if single unit",
            required=False,
        ),
        "floors": Integer(
            default=1, title="Stories", description="Number of stories", required=True
        ),
        "pool": Nested(
            {
                "has_pool": Boolean(
                    default=False,
                    title="Pool",
                    description="Property has a private pool",
                    required=True,
                ),
                "pool_size": Integer(
                    title="Pool Size", description="Pool area", required=False
                ),
            },
            title="Pool Data",
            allow_null=False,
            skip_none=False,
        ),
        "parking": Nested(
            {
                "garage": Integer(
                    default=0,
                    title="Garage Spots",
                    description="Number of spots in a garage",
                    required=True,
                ),
                "covered": Integer(
                    default=0,
                    title="Covered Spots",
                    description="Number of top-covered spots",
                    required=True,
                ),
                "uncovered": Integer(
                    default=0,
                    title="Uncovered Spots",
                    description="Number of uncovered, non-street spots",
                    required=True,
                ),
            },
            allow_null=False,
            skip_none=False,
            required=True,
        ),
        "parent": String(
            title="Parent Address",
            description="Parent UUID, if it is part of another address",
            required=False,
        ),
        "children": List(
            String(
                title="Children Address",
                description="Children UUID, if it has subdivided units",
                required=False,
            ),
            required=False,
        ),
    },
    strict=True,
)
