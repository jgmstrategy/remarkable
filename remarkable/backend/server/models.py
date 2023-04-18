"""Global models initializer"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column

from remarkable.backend.util.uuid import GUID, default_uuid

db = SQLAlchemy()


# mypy: disable-error-code=name-defined
# pylint: disable=too-few-public-methods
class Base(db.Model):
    """Base model for UUID usage"""

    __abstract__ = True

    id: Column = db.Column(GUID(), primary_key=True, default=default_uuid)
    created_at: Column = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at: Column = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
