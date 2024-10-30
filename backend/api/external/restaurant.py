from core.settings import ProjectSettings
from services.restaurant import RestaurantService
from fastapi import APIRouter, status

from schemas.input_create_restaurant import InputCreateRestaurant
from schemas.restaurant import Restaurant

router = APIRouter()

@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=Restaurant
)
async def create_restaurant(
    input_create_restaurant: InputCreateRestaurant
):
    return RestaurantService.create(input_create_restaurant)


@router.get(
    "/get/{restaurant_id}",
    response_model=int
)
async def get_restaurant(
    restaurant_id: int
):
    settings = ProjectSettings()
    return settings.TEST