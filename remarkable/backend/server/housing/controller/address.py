"""Address controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.config.address import (
    address_by_id_args,
    neighborhood_args,
    owner_args,
)
from remarkable.backend.server.housing.models.address import (
    address,
    api,
    neighborhood,
    owner,
)


@api.route("/owner")
class Owner(Resource):
    """Owners as a resource"""

    @api.doc("get_owner")
    @api.expect(owner_args)
    @api.marshal_with(owner)
    def get(self) -> dict:
        """Get an owner"""
        api.abort(404)
        return {}

    @api.doc("create_owner")
    @api.expect(owner)
    def post(self) -> None:
        """Create an owner"""
        api.abort(404)


@api.route("/neighborhood")
class Neighborhood(Resource):
    """Neighborhoods as a resource"""

    @api.doc("get_neighborhood")
    @api.expect(neighborhood_args)
    @api.marshal_with(neighborhood)
    def get(self) -> dict:
        """Get a neighborhood"""
        api.abort(404)
        return {}

    @api.doc("create_neighborhood")
    @api.expect(neighborhood)
    def post(self) -> None:
        """Create a neighborhood"""
        api.abort(404)


@api.route("/")
class Address(Resource):
    """Address as a resource"""

    @api.doc("get_address")
    @api.expect(address_by_id_args)
    @api.marshal_with(address)
    def get(self) -> dict:
        """Get an address"""
        api.abort(404)
        return {}

    @api.doc("create_address")
    @api.expect(address)
    def post(self) -> None:
        """Create an address"""
        api.abort(404)
