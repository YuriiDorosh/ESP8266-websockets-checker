from database.base import Base
from database.mixins.id import IdMixin
from database.mixins.timestamp import TimestampMixin
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base, IdMixin, TimestampMixin):
    __tablename__ = "users"

    telegram_tag: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
