import os
from telethon.tl.types import Message
from telethon.errors import ChannelInvalidError
from src.file_handler import FileHandler
from src.logger import setup_logger

logger = setup_logger()

class GroupHandler:
    def __init__(self, client):
        self.client = client

    async def process_group_messages(self, group_link):
        """
        Process all messages from the specified group. Save the sender's username or ID
        to a file named after the group.
        """
        try:
            # Connect to the group
            entity = await self.client.get_entity(group_link)
            group_name = self._sanitize_group_name(entity.title)
            file_handler = FileHandler(group_name)

            # Process messages
            async for message in self.client.iter_messages(entity, reverse=True):
                if isinstance(message, Message) and message.sender_id:
                    sender = await self.client.get_entity(message.sender_id)
                    username_or_id = self._get_username_or_id(sender)
                    file_handler.save_user(username_or_id)

            logger.info(f"Processed all messages from group: {group_name}")

        except ChannelInvalidError:
            logger.error("Invalid group link or ID provided.")
        except Exception as e:
            logger.error(f"Error processing group messages: {e}")

    def _sanitize_group_name(self, group_name):
        """
        Sanitize the group name by removing any non-alphanumeric characters.
        """
        return "".join(char if char.isalnum() or char.isspace() else "" for char in group_name)

    def _get_username_or_id(self, sender):
        """
        Get the sender's username or ID. If the sender has a username, return it with an '@' prefix.
        Otherwise, return the sender's ID as a Telegram link.
        """
        if sender.username:
            return f"@{sender.username}"
        else:
            return f"https://t.me/{sender.id}"
