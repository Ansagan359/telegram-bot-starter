"""Shared commands and menu callbacks (/help, About, navigation)."""

from __future__ import annotations

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from ..keyboards.inline import back_menu, main_menu

router = Router(name="common")

MENU_TEXT = "🏠 <b>Main menu</b>\n\nPick an option below."

HELP_TEXT = (
    "ℹ️ <b>Help</b>\n\n"
    "Available commands:\n"
    "• /start — open the main menu\n"
    "• /help — show this message\n\n"
    "Send any text and the bot will echo it back."
)

ABOUT_TEXT = (
    "✨ <b>About</b>\n\n"
    "A minimal, production-ready Telegram bot template built with "
    "<b>aiogram 3</b>: typed config, routers, middlewares and Docker support.\n\n"
    "Fork it and start shipping your own bot in minutes."
)


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(HELP_TEXT, reply_markup=back_menu())


@router.callback_query(F.data == "menu:help")
async def cb_help(callback: CallbackQuery) -> None:
    if isinstance(callback.message, Message):
        await callback.message.edit_text(HELP_TEXT, reply_markup=back_menu())
    await callback.answer()


@router.callback_query(F.data == "menu:about")
async def cb_about(callback: CallbackQuery) -> None:
    if isinstance(callback.message, Message):
        await callback.message.edit_text(ABOUT_TEXT, reply_markup=back_menu())
    await callback.answer()


@router.callback_query(F.data == "menu:home")
async def cb_home(callback: CallbackQuery) -> None:
    if isinstance(callback.message, Message):
        await callback.message.edit_text(MENU_TEXT, reply_markup=main_menu())
    await callback.answer()
