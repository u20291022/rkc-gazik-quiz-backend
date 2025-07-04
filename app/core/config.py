from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"
    ENABLE_REQUEST_LOGGING: bool = True
    LOG_SQL_QUERIES: bool = False
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str
    TELEGRAM_LOG_LEVEL: str = "INFO"
    ENABLE_TELEGRAM_LOGGING: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
    "timezone": "UTC",
}
