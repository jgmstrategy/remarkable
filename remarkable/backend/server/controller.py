"""Controller/API"""

from flask_restx import Api

import remarkable.backend.server.housing.controller.address as address_controller
import remarkable.backend.server.housing.controller.rent as rent_controller
import remarkable.backend.server.housing.controller.sale as sale_controller

api = Api(
    title="remarkable backend API", version="1.0", description="remarkable backend API"
)

api.add_namespace(address_controller.api)
api.add_namespace(rent_controller.api)
api.add_namespace(sale_controller.api)
