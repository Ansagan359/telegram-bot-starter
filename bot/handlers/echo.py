"""Fallback echo handler — must be registered last."""

from __future__ import annotations

from aiogram import F, Router
from aiogram.types import Message

router = Router(name="echo")


@router.message(F.text & ~F.text.startswith("/"))
async def echo(message: Message) -> None:
    """Echo any non-command text back to the user."""
    await message.answer(
        f"You said:\n<blockquote>{message.html_text}</blockquote>"
    )


@router.message()
async def fallback(message: Message) -> None:
    """Catch non-text content (stickers, photos, etc.)."""
    await message.answer("I can only handle text for now 🙂")
