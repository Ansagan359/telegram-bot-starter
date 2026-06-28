"""/start command."""

from __future__ import annotations

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from ..keyboards.inline import main_menu

router = Router(name="start")

WELCOME = (
    "👋 <b>Welcome, {name}!</b>\n\n"
    "This is a <b>Telegram Bot Starter</b> — a clean, production-ready "
    "boilerplate built with <b>aiogram 3</b>.\n\n"
    "Use the menu below, or send me any message and I'll echo it back."
)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Greet the user and show the main menu."""
    name = message.from_user.full_name if message.from_user else "there"
    await message.answer(WELCOME.format(name=name), reply_markup=main_menu())
