from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os 

class ProjectSettings(BaseSettings):
    load_dotenv()

    MongoDBConnectionString: str = os.getenv("MongoDBConnectionString")
    MongoDBName: str = os.getenv("MongoDBName")

    FrontendURL: str = os.getenv("FrontendURL")
    
    class Config:
        env_file = ".env"