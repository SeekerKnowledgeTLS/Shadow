import asyncio
from .config import bot

async def main():
    bot.infinity_polling(timeout= 10)

if __name__ == "__main__":
    asyncio.run(main())