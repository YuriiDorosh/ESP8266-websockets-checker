import uuid

from sqlalchemy import UUID, Column
from sqlalchemy.ext.declarative import declared_attr


class IdMixin:
    @declared_attr
    def id(cls):
        return Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
