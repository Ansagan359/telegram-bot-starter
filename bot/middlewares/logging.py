"""Update logging middleware."""

from __future__ import annotations

import logging
from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    """Log a short summary of every incoming update."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, Update) and event.message:
            user = event.message.from_user
            who = f"{user.id} (@{user.username})" if user else "unknown"
            logger.info("message from %s: %r", who, event.message.text)
        return await handler(event, data)
