from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base
from database.mixins.timestamp import TimestampMixin
from database.mixins.id import IdMixin


class Wifi(Base, IdMixin, TimestampMixin):
    __tablename__ = 'wifi'

    is_powered: Mapped[bool] = mapped_column(Boolean, default=False)
