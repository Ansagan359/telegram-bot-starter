"""Inline keyboards."""

from __future__ import annotations

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

REPO_URL = "https://github.com/Ansagan359/telegram-bot-starter"


def main_menu() -> InlineKeyboardMarkup:
    """Primary menu shown on /start."""
    builder = InlineKeyboardBuilder()
    builder.button(text="ℹ️ Help", callback_data="menu:help")
    builder.button(text="✨ About", callback_data="menu:about")
    builder.button(text="⭐ Source code", url=REPO_URL)
    builder.adjust(2, 1)
    return builder.as_markup()


def back_menu() -> InlineKeyboardMarkup:
    """A single 'back to menu' button."""
    builder = InlineKeyboardBuilder()
    builder.button(text="← Back", callback_data="menu:home")
    return builder.as_markup()
