from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings with environment variables support."""

    # Database
    database_url: str = "postgresql+asyncpg://events_user:events_pass@localhost:5432/events_db"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # API
    api_title: str = "Events Analytics API"
    api_version: str = "1.0.0"
    api_rate_limit: int = 100
    api_rate_limit_window: int = 60

    # Logging
    log_level: str = "INFO"

    # Performance
    db_pool_size: int = 20
    db_max_overflow: int = 10
    batch_insert_size: int = 1000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
