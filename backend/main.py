from fastapi import FastAPI
from external.restaurant import router as restaurant_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(restaurant_router, prefix="/restaurant", tags=["restaurant"])