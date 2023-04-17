from flask_restx import Namespace  # type: ignore
from flask_restx.fields import Boolean, String  # type: ignore

api = Namespace("address", description="Location related operations")

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
)

address = api.model(
    "Address",
    {
        "id": String(
            title="Location ID", description="UUID of location", required=True
        ),
        "name": String(
            title="Name", description="Friendly name of community", required=False
        ),
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
    },
)
