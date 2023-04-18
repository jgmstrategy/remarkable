"""Models for local addressing"""

from flask_restx import Namespace
from flask_restx.fields import Boolean, Float, Integer, List, Nested, String

api = Namespace("address", description="Location related operations")

owner = api.model(
    "Owner",
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
        "community": String(
            title="Community",
            description="UUID of community",
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
