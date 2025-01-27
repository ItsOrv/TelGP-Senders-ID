from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_NAME
from src.logger import setup_logger
import os

logger = setup_logger()

class TelegramSession:
    def __init__(self):
        self.client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
        self.session_file = f"{SESSION_NAME}.session"

    async def login(self):
        """
        Attempt to log in using an existing session. If the session is not authorized,
        start a new session by prompting the user for their phone number, code, and password.
        """
        try:
            if os.path.exists(self.session_file):
                await self.client.connect()
                if not await self.client.is_user_authorized():
                    raise Exception("Session is not authorized.")
            else:
                await self._start_new_session()
            logger.info("Logged in successfully.")
            return self.client
        except Exception as e:
            logger.error(f"Failed to log in with existing session: {e}")
            if os.path.exists(self.session_file):
                os.remove(self.session_file)
            return await self._start_new_session()

    async def _start_new_session(self):
        """
        Start a new session by prompting the user for their phone number, code, and password.
        """
        try:
            await self.client.start(
                phone=lambda: input("Enter your phone number: "),
                code_callback=lambda: input("Enter the code you received: "),
                password=lambda: input("Enter your password: ")
            )
            logger.info("Logged in successfully with new session.")
            return self.client
        except Exception as e:
            logger.error(f"Failed to log in with new session: {e}")
            raise

    async def logout(self):
        """
        Log out and disconnect the client.
        """
        try:
            await self.client.disconnect()
            logger.info("Logged out successfully.")
        except Exception as e:
            logger.error(f"Failed to log out: {e}")
            raise
