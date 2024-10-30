from db.repositories.restaurant import RestaurantRepository
from core.dependencies import get_mongo_ds
from core.settings import ProjectSettings
from services.restaurant import RestaurantService
from fastapi import APIRouter, status, Depends

from schemas.input_create_restaurant import InputCreateRestaurant
from schemas.restaurant import Restaurant

router = APIRouter()

@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=Restaurant
)
async def create_restaurant(
    input_create_restaurant: InputCreateRestaurant,
    mongo_ds=Depends(get_mongo_ds)
):
    restaurant_id = RestaurantService.create_restaurant(input_create_restaurant=input_create_restaurant,
                                               restaurant_repository=RestaurantRepository(mongo_ds))

    return Restaurant(restaurant_id=restaurant_id)
