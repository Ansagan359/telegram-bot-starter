"""Application entry point: ``python -m bot``."""

from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .config import get_settings
from .handlers import get_routers
from .middlewares.logging import LoggingMiddleware
from .utils.logging import setup_logging


async def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)
    logger = logging.getLogger("bot")

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.update.outer_middleware(LoggingMiddleware())
    dp.include_routers(*get_routers())

    me = await bot.get_me()
    logger.info("Starting @%s (id=%s)…", me.username, me.id)

    try:
        await bot.delete_webhook(drop_pending_updates=settings.drop_pending_updates)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        logger.info("Bot stopped.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
