"""Models for units listed for sale"""

from flask_restx import Namespace  # type: ignore
from flask_restx.fields import String  # type: ignore

api = Namespace("sale", "Sale price related operations")

listing = api.model("listing", {})
