from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL = "postgresql://user:password@db:5432/taskdb"
    SECRET_KEY: str = "supersecret"

    class Config:
        env_file = ".env"

settings = Settings()