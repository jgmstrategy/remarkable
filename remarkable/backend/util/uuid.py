"""UUID for SQLite in SQLAlchemy"""

import uuid
from typing import Any, Optional, Union

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.engine import Dialect
from sqlalchemy.types import CHAR, TypeDecorator, TypeEngine


def default_uuid():
    """Return a UUID"""
    return str(uuid.uuid4())


# pylint: disable=too-many-ancestors, abstract-method
class GUID(TypeDecorator):
    """GUID generator for SQLAlchemy"""

    impl = CHAR

    def load_dialect_impl(
        self, dialect: Dialect
    ) -> Union[TypeEngine[uuid.UUID], TypeEngine[str]]:
        if dialect.name == "postgresql":
            return dialect.type_descriptor(UUID())

        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value: Optional[str], dialect: Dialect) -> Any:
        if value is None:
            return value

        if dialect.name == "postgresql":
            return str(value)

        if not isinstance(value, uuid.UUID):
            return f"{uuid.UUID(value).int:.32x}"

        return f"{value.int:.32x}"

    def process_result_value(self, value: Optional[Any], dialect: Dialect) -> Any:
        if value is None:
            return value

        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)

        return value
