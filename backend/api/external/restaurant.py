from db.repositories.restaurant import RestaurantRepository
from core.dependencies import get_mongo_ds
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
    mongo_id = RestaurantService.create_restaurant(input_create_restaurant=input_create_restaurant,
                                               restaurant_repository=RestaurantRepository(mongo_ds))

    return Restaurant(
        mongo_id = mongo_id,
        name = input_create_restaurant.name,
        latitude = input_create_restaurant.latitude,
        longitude = input_create_restaurant.longitude,
        address = input_create_restaurant.address,
        phone_number = input_create_restaurant.phone_number,
        email = input_create_restaurant.email,
        instagram = input_create_restaurant.instagram,
        timetable = input_create_restaurant.timetable
    )
