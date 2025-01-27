import logging
from config import LOG_FILE

def setup_logger():
    """
    Set up the logger for the application. Ensure that the logger is set up only once
    to avoid duplicate log entries.
    """
    logger = logging.getLogger("TelegramUserSaver")
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
