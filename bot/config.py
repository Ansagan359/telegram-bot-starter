"""Application configuration loaded from environment variables / .env."""

from __future__ import annotations

from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Strongly-typed settings.

    Values are read from environment variables (or a local ``.env`` file).
    See ``.env.example`` for the full list.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    bot_token: str
    """Bot token issued by @BotFather."""

    admin_ids: list[int] = []
    """Telegram user IDs allowed to use admin-only features."""

    log_level: str = "INFO"
    """Root logging level (DEBUG, INFO, WARNING, ...)."""

    drop_pending_updates: bool = True
    """Skip updates that arrived while the bot was offline."""

    @field_validator("admin_ids", mode="before")
    @classmethod
    def _parse_admin_ids(cls, value: object) -> object:
        """Allow ADMIN_IDS to be a comma-separated string like ``1,2,3``."""
        if isinstance(value, str):
            return [int(part) for part in value.replace(" ", "").split(",") if part]
        return value


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()  # type: ignore[call-arg]
