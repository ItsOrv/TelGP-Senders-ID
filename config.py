import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    API_ID = os.getenv("API_ID", "default_api_id")
    API_HASH = os.getenv("API_HASH", "default_api_hash")
    SESSION_NAME = os.getenv("SESSION_NAME", "telegram_user_saver")
    LOG_FILE = os.getenv("LOG_FILE", "app.log")

    if not API_ID or not API_HASH:
        raise ValueError("API_ID and API_HASH must be set in the .env file")

except Exception as e:
    raise RuntimeError(f"Error loading configuration: {e}")
