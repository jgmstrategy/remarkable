"""Address controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.models.address import (
    address,
    api,
    neighborhood,
    owner,
)


# pylint: disable=redefined-builtin
# pylint: disable=unused-argument
@api.route("/owner/create")
class CreateOwner(Resource):
    """Create an owner"""

    @api.doc("create_owner")
    @api.expect(owner)
    def post(self) -> None:
        """Create an owner"""
        api.abort(404)


@api.route("/owner/id/<id>")
@api.param("id", "UUID of owner")
class Owner(Resource):
    """Owners as a resource"""

    @api.doc("get_owner")
    @api.marshal_with(owner)
    def get(self, id) -> dict:
        """Get an owner"""
        api.abort(404)
        return {}


@api.route("/neighborhood/create")
class CreateNeighborhood(Resource):
    """Create a neighborhood"""

    @api.doc("create_neighborhood")
    @api.expect(neighborhood)
    def post(self) -> None:
        """Create a neighborhood"""
        api.abort(404)


@api.route("/neighborhood/id/<id>")
@api.param("id", "UUID of neighborhood")
class Neighborhood(Resource):
    """Neighborhoods as a resource"""

    @api.doc("get_neighborhood")
    @api.marshal_with(neighborhood)
    def get(self, id) -> dict:
        """Get a neighborhood"""
        api.abort(404)
        return {}


@api.route("/create")
class CreateAddress(Resource):
    """Create an address"""

    @api.doc("create_address")
    @api.expect(address)
    def post(self) -> None:
        """Create an address"""
        api.abort(404)


@api.route("/id/<id>")
@api.param("id", "UUID of address")
class Address(Resource):
    """Address as a resource"""

    @api.doc("get_address")
    @api.marshal_with(address)
    def get(self, id) -> dict:
        """Get an address"""
        api.abort(404)
        return {}
