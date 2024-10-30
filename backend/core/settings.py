from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class ProjectSettings(BaseSettings):
    load_dotenv()

    MongoDBHost: str
    MongoDBPort: str
    MongoDBUser: str
    MongoDBPassword: str
    
    class Config:
        env_file = ".env"