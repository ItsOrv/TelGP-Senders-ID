import asyncio
from telethon.errors import SessionPasswordNeededError
from src.session_handler import TelegramSession
from src.group_handler import GroupHandler
from src.logger import setup_logger

# Set up logging
logger = setup_logger()

async def main():
    """
    Main function to log in to Telegram, process group messages, and log out.
    """
    session = None
    try:
        # Log in to Telegram
        session = TelegramSession()
        client = await session.login()

        # Get the group link from the user
        group_link = input("Enter the group link/ID/name: ").strip()

        # Process the group messages
        group_handler = GroupHandler(client)
        await group_handler.process_group_messages(group_link)

    except SessionPasswordNeededError:
        logger.error("Two-step verification required. Please try again and enter your password when prompted.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        if session:
            try:
                await session.logout()
            except Exception as e:
                logger.error(f"Error during logout: {e}")

if __name__ == "__main__":
    asyncio.run(main())
