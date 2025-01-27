import os
from src.logger import setup_logger

logger = setup_logger()

class FileHandler:
    def __init__(self, group_name):
        self.file_name = f"{group_name}.txt"
        self.existing_users = self._load_existing_users()

    def _load_existing_users(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as file:
                return set(line.strip() for line in file)
        return set()

    def save_user(self, user_info):
        if user_info not in self.existing_users:
            try:
                with open(self.file_name, "a", encoding="utf-8") as file:
                    file.write(user_info + "\n")
                self.existing_users.add(user_info)
                logger.info(f"Saved user: {user_info}")
            except Exception as e:
                raise IOError(f"Error saving user info: {e}")
