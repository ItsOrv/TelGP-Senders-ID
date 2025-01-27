import os

class FileHandler:
    def __init__(self, group_name):
        self.file_name = f"{group_name}.txt"

    def save_user(self, user_info):
        try:
            with open(self.file_name, "a", encoding="utf-8") as file:
                file.write(user_info + "\n")
        except Exception as e:
            raise IOError(f"Error saving user info: {e}")
