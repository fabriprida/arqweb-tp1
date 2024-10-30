from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class ProjectSettings(BaseSettings):
    load_dotenv()

    class Config:
        env_file = ".env"