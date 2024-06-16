import os

from dotenv import load_dotenv

load_dotenv()


class BotConfig:
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")

    def get_token(self) -> str:
        return self.token
