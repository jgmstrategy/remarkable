"""Controller/API"""

from flask_restx import Api

from remarkable.backend.server.housing.controller.address import api as address_api

from remarkable.backend.server.housing.models.rent import api as rent_api
from remarkable.backend.server.housing.models.sale import api as sale_api


api = Api(
    title="remarkable backend API", version="1.0", description="remarkable backend API"
)

api.add_namespace(address_api)
api.add_namespace(rent_api)
api.add_namespace(sale_api)