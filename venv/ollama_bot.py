import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from engine import Llama3Engine
from aiogram.utils.chat_action import ChatActionMiddleware

class Llama3Bot:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TOKEN")
        if not self.token:
            raise ValueError("Token not found (telegram)")

        self.bot = Bot(token=self.token)
        self.dp = Dispatcher()
        self.ai = Llama3Engine()

    async def run(self) -> None:
        await self.dp.start_polling(self.bot)