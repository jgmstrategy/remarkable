"""Sale controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.models.sale import api, listing


@api.route("/create")
class CreateListing(Resource):
    """Create a sale entry"""

    @api.doc("create_listing")
    @api.expect(listing)
    def post(self) -> None:
        """Create a listing"""
        api.abort(404)


@api.route("/id/<id>")
class Listing(Resource):
    """Real estate as a resource"""

    @api.doc("get_listing")
    @api.marshal_with(listing)
    def get(self) -> dict:
        """Get a listing"""
        api.abort(404)
        return {}
