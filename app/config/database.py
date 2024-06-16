import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


class DatabaseConfig:
    def __init__(self) -> None:
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.name = os.getenv("DB_NAME")

    def get_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@db/{self.host}"

    def _get_engine(self) -> AsyncSession:
        return create_async_engine(self.get_url())

    def get_session(self) -> sessionmaker:
        return sessionmaker(
            self._get_engine(), expire_on_commit=False, class_=AsyncSession
        )
