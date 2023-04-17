"""Controller/API"""

from flask_restx import Api  # type: ignore

api = Api(
    title="remarkable backend API", version="1.0", description="remarkable backend API"
)
