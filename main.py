import asyncio
from src.session_handler import TelegramSession
from src.group_handler import GroupHandler
from src.logger import setup_logger

# تنظیم لاگ‌ها
logger = setup_logger()

async def main():
    try:
        # ورود به تلگرام
        session = TelegramSession()
        client = await session.login()

        # گرفتن لینک گروه از کاربر
        group_link = input("Enter the group link/ID/name: ").strip()

        # پردازش گروه
        group_handler = GroupHandler(client)
        await group_handler.process_group_messages(group_link)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        await session.logout()

if __name__ == "__main__":
    asyncio.run(main())
