import os

from dotenv import load_dotenv

load_dotenv()


class RedisConfig:
    def __init__(self) -> None:
        self.host = os.getenv("REDIS_HOST")
        self.port = os.getenv("REDIS_PORT")
        self.password = os.getenv("REDIS_PASSWORD")
        self.db = os.getenv("REDIS_DB")

    def get_url(self) -> str:
        return f"redis://{self.host}:{self.port}"
