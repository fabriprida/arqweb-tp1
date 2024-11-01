from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.external.restaurant import router as restaurant_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # Allow frontend to access the backend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(restaurant_router, prefix="/internal/restaurant", tags=["restaurant"])