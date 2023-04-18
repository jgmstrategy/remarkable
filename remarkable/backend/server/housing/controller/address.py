"""Address controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.models.address import api, address


@api.route("/<id>")
@api.param("id", "UUID of address")
class Address(Resource):
    @api.doc("get_address")
    @api.marshal_with(address)
    def get(self, id):
        return {
            "id": "00000000-0000-0000-0000-000000000000",
            "mls": "0",
            "name": "Example",
            "number": "1234",
            "street": "Main St",
            "zip": "12345",
            "county": "New York",
            "city": "New York",
            "state": "NY",
            "country": "USA",
            "units": 1,
            "floors": 1,
            "pool": {"has_pool": False},
            "parking": {"garage": 1, "covered": 1, "uncovered": 2},
        }
