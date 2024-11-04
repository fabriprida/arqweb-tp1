from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os 

class ProjectSettings(BaseSettings):
    load_dotenv()

    MongoDBHost: str = os.getenv("MongoDBHost")
    MongoDBPort: str = os.getenv("MongoDBPort")
    MongoDBUser: str = os.getenv("MongoDBUser")
    MongoDBPassword: str = os.getenv("MongoDBPassword")
    MongoDBName: str = os.getenv("MongoDBName")

    FrontendURL: str = os.getenv("FrontendURL")
    
    class Config:
        env_file = ".env"