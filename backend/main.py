from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.external.restaurant import router as restaurant_router
from core.settings import ProjectSettings

app = FastAPI()


project_settings = ProjectSettings()
origins = [
    project_settings.FrontendURL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(restaurant_router, prefix="/internal/restaurant", tags=["restaurant"])