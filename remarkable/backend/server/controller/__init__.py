"""Controller/API"""

# mypy: disable-error-code="import"
from flask_restx import Api

api = Api(
    title="remarkable backend API", version="1.0", description="remarkable backend API"
)
