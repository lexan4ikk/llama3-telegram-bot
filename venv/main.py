from aiogram import types, Router, filters
from aiogram.filters import CommandStart, Command
from aiogram.utils.chat_action import ChatActionSender
from loader import bot_manager
import asyncio

router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer('Hi! I’m your AI assistant based on the Llama 3 model. I’ll help you with your day-to-day tasks. Enter command "/help" to show all commands')

@router.message(Command('help'))
async def help(message: types.Message) -> None:
    await message.answer('Available commands:\n' \
                         '/start - start the bot\n' \
                         '/help - show available commands\n' \
                         '/prompt [text] - ask the assistant\n' \
                         '/forgot - clear the last dialogue\n' \
                         '/load - restore the last dialogue\n')
    
@router.message(Command('prompt'))
async def prompt(message: types.Message, command: filters.CommandObject) -> None:
    user_prompt = command.args

    if not user_prompt:
        await message.answer(
            "No request text provided.\n"
            "Example: <code>/prompt your prompt for the assistant</code>",
            parse_mode="HTML"
        )
        return

    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        response = await bot_manager.ai.ask(message.from_user.id, user_prompt)
    await message.answer(response)


@router.message(Command('forgot'))
async def forgot(message: types.Message) -> None:
    try:
        await bot_manager.ai.delete_context(message.from_user.id)
        await message.answer("Delete context success")
    except Exception as e:
        print(f"Error: {e} (delete context)")
        await message.answer("Error deleting context")

@router.message(Command('load'))
async def load(message: types.Message) -> None:
    try:
        await bot_manager.ai.load_context(message.from_user.id)
        await message.answer("Load context success")
    except Exception as e:
        print(f"Error: {e} (load context from database)")
        await message.answer("Error loading context")

if __name__ == "__main__":
    bot_manager.dp.include_router(router)
    asyncio.run(bot_manager.run())