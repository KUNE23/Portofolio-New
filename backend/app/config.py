from functools import lru_cache
import os


class Settings:
    def __init__(self) -> None:
        self.database_url = self._required("DATABASE_URL")
        self.admin_token = self._required("ADMIN_TOKEN")
        self.allowed_origins = self._csv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
        self.rate_limit_requests = int(os.getenv("RATE_LIMIT_REQUESTS", "120"))
        self.rate_limit_window_seconds = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60"))

    @staticmethod
    def _required(name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise RuntimeError(f"{name} environment variable is required")
        return value

    @staticmethod
    def _csv(name: str, default: str) -> list[str]:
        raw = os.getenv(name, default)
        return [item.strip() for item in raw.split(",") if item.strip()]

    @property
    def async_database_url(self) -> str:
        if self.database_url.startswith("sqlite"):
            return self.database_url
        if self.database_url.startswith("postgresql+asyncpg://"):
            return self.database_url
        if self.database_url.startswith("postgresql://"):
            return self.database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
        if self.database_url.startswith("postgres://"):
            return self.database_url.replace("postgres://", "postgresql+asyncpg://", 1)
        return self.database_url


@lru_cache
def get_settings() -> Settings:
    return Settings()
