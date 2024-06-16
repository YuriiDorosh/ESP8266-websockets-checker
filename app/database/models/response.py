from database.base import Base
from database.mixins.id import IdMixin
from database.mixins.timestamp import TimestampMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Response(Base, IdMixin, TimestampMixin):
    __tablename__ = "responses"

    signal_strength: Mapped[int] = mapped_column(Integer, nullable=False)
    mac_address: Mapped[str] = mapped_column(String, nullable=True)
