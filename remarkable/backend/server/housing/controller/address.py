"""Address controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.models.address import address, api


@api.route("/<id>")
@api.param("id", "UUID of address")
class Address(Resource):
    """Address as a resource"""

    @api.doc("get_address")
    @api.marshal_with(address)
    def get(self, id):
        """Get an address"""
        api.abort(404)
