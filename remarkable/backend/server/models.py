"""Global models initializer"""

import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped

from remarkable.backend.util.uuid import GUID, default_uuid

db = SQLAlchemy()


# mypy: disable-error-code=name-defined
# pylint: disable=too-few-public-methods
class Base(db.Model):
    """Base model for UUID usage"""

    __abstract__ = True

    id: Mapped[str] = db.Column(GUID(), primary_key=True, default=default_uuid)
    created_at: Mapped[datetime.datetime] = db.Column(
        db.DateTime, default=db.func.current_timestamp()
    )
    updated_at: Mapped[datetime.datetime] = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )


def add_and_commit(obj: Base, database: SQLAlchemy = db) -> str:
    """Adds and commits an object to the database"""
    database.session.add(obj)
    database.session.commit()
    return obj.id
