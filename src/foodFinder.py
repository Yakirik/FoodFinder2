import asyncio
import logging

from aiogram import Dispatcher, Bot
from config import BOT_TOKEN
from handlers import router as main_router


class FoodFinderBot:
    def __init__(self, token):
        self.bot = Bot(token)

        logging.basicConfig(level=logging.INFO)
        self.dispatcher = Dispatcher()

        self.dispatcher.include_router(main_router)

    async def main(self):
        await self.dispatcher.start_polling(self.bot)


if __name__ == "__main__":
    botik = FoodFinderBot(BOT_TOKEN)

    asyncio.run(botik.main())
