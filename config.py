from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BenderCopilot"
    ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    class Config:
        env_file = ".env"

settings = Settings()