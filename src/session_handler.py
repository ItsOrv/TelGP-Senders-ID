from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_NAME
from utils.logger import setup_logger

logger = setup_logger()

class TelegramSession:
    def __init__(self):
        self.client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    async def login(self):
        try:
            await self.client.start()
            logger.info("Logged in successfully.")
            return self.client
        except Exception as e:
            logger.error(f"Failed to log in: {e}")
            raise
