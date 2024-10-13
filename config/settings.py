import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings():
    PROJECT_TITLE: str = "Job Board"
    PROJECT_VERSION: str = "0.1.0"

    # DB Settings
    DATABASE_USER: str = os.getenv("DB_USER", "postgres.username")
    DATABASE_PASSWORD: str = os.getenv("DB_PASSWORD", "PASSWORD")
    DATABASE_HOST: str = os.getenv("DB_HOST", "HOST")
    DATABASE_PORT: str = os.getenv("DB_PORT", "PORT")
    DATABASE_NAME: str = os.getenv("DB_NAME", "NAME")
    DATABASE_URL: str = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


settings = Settings()
