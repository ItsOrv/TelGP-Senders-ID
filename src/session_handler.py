from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from config import API_ID, API_HASH, SESSION_NAME
from src.logger import setup_logger
import os
import stat

logger = setup_logger()

class TelegramSession:
    def __init__(self):
        self.client = None
        self.session_file = f"{SESSION_NAME}.session"
        self._ensure_writable_session()

    def _ensure_writable_session(self):
        """Ensure the session directory and file are writable"""
        session_dir = os.path.dirname(os.path.abspath(self.session_file))
        os.makedirs(session_dir, exist_ok=True)
        
        # Set directory permissions
        try:
            os.chmod(session_dir, 0o755)
        except Exception as e:
            logger.warning(f"Could not set directory permissions: {e}")

        # Set file permissions if it exists
        if os.path.exists(self.session_file):
            try:
                os.chmod(self.session_file, 0o600)
            except Exception as e:
                logger.warning(f"Could not set file permissions: {e}")
                self._remove_session_file()

    def _remove_session_file(self):
        """Safely remove the session file"""
        try:
            if os.path.exists(self.session_file):
                os.remove(self.session_file)
                logger.info("Removed existing session file")
        except Exception as e:
            logger.error(f"Failed to remove session file: {e}")

    async def login(self):
        """
        Attempt to log in using an existing session or create a new one.
        """
        try:
            self.client = TelegramClient(self.session_file, API_ID, API_HASH)
            
            await self.client.connect()
            if not await self.client.is_user_authorized():
                await self._start_new_session()
            
            logger.info("Logged in successfully")
            return self.client
            
        except Exception as e:
            logger.error(f"Login failed: {e}")
            self._remove_session_file()
            raise

    async def _start_new_session(self):
        """Start a new session with support for two-step verification"""
        try:
            phone = input("Enter your phone number: ")
            await self.client.send_code_request(phone)
            code = input("Enter the code you received: ")
            
            try:
                await self.client.sign_in(phone, code)
            except SessionPasswordNeededError:
                # Handle two-step verification
                password = input("Two-step verification enabled. Please enter your password: ")
                await self.client.sign_in(password=password)
                
        except Exception as e:
            logger.error(f"Failed to start new session: {e}")
            raise

    async def logout(self):
        """Safely logout and disconnect"""
        if self.client:
            try:
                await self.client.disconnect()
                logger.info("Logged out successfully")
            except Exception as e:
                logger.error(f"Error during logout: {e}")
                # If we get a readonly error during logout, remove the session file
                if "readonly database" in str(e).lower():
                    self._remove_session_file()
