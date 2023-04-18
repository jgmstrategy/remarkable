"""Rent controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.config.rent import entry_params
from remarkable.backend.server.housing.models.rent import api, entry


@api.route("/")
class Entry(Resource):
    """Entries as a resource"""

    @api.doc("get_entry")
    @api.expect(entry_params)
    @api.marshal_with(entry)
    def get(self) -> dict:
        """Get an entry"""
        api.abort(404)
        return {}

    @api.doc("create_entry")
    @api.expect(entry)
    def post(self) -> None:
        """Create an entry"""
        api.expect(404)
