from fastapi import FastAPI
from external.restaurant import router as restaurant_router

app = FastAPI()

app.include_router(restaurant_router, prefix="/restaurant")