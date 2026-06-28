"""Handler routers, exposed in registration order."""

from __future__ import annotations

from aiogram import Router

from . import common, echo, start


def get_routers() -> list[Router]:
    """Return routers in priority order (echo must come last)."""
    return [start.router, common.router, echo.router]
