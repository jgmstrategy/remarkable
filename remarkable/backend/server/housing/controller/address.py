"""Address controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.models.address import address, api


@api.route("/create")
class CreateAddress(Resource):
    """Create an address"""

    @api.doc("create_address")
    @api.expect(address)
    def post(self) -> dict:
        """Create an address"""
        api.abort(404)


@api.route("/<id>")
@api.param("id", "UUID of address")
class Address(Resource):
    """Address as a resource"""

    @api.doc("get_address")
    @api.marshal_with(address)
    def get(self, id) -> dict:
        """Get an address"""
        api.abort(404)
