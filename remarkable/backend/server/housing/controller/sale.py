"""Sale controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.config.sale import listing_params
from remarkable.backend.server.housing.models.sale import api, listing


@api.route("/")
class ListingById(Resource):
    """Real estate as a resource"""

    @api.doc("get_listing")
    @api.expect(listing_params)
    @api.marshal_with(listing)
    def get(self) -> dict:
        """Get a listing"""
        api.abort(404)
        return {}

    @api.doc("create_listing")
    @api.expect(listing)
    def post(self) -> None:
        """Create a listing"""
        api.abort(404)
