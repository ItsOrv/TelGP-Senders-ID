import logging
from config import LOG_FILE

def setup_logger():
    logger = logging.getLogger("TelegramUserSaver")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
