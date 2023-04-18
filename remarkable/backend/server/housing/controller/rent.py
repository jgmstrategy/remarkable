"""Rent controller"""

from flask_restx import Resource

from remarkable.backend.server.housing.models.rent import api, entry


# pylint: disable=redefined-builtin
# pylint: disable=unused-argument
@api.route("/create")
class CreateEntry(Resource):
    """Create a rent entry"""

    @api.doc("create_entry")
    @api.expect(entry)
    def post(self) -> None:
        """Create an entry"""
        api.expect(404)


@api.route("/id/<id>")
class EntryById(Resource):
    """Entries as a resource"""

    @api.doc("get_entry_by_id")
    @api.marshal_with(entry)
    def get(self, id) -> dict:
        """Get an entry"""
        api.abort(404)
        return {}
