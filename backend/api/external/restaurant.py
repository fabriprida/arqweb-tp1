from schemas.menu import MenuItem, Menu
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
    return RestaurantService.create_restaurant(input_create_restaurant=input_create_restaurant,
                                               restaurant_repository=RestaurantRepository(mongo_ds))

    


@router.post(
    "/{restaurant_id}/menu",
    status_code=status.HTTP_201_CREATED,
    response_model=Menu
)
async def add_menu_item_to_menu(
    restaurant_id: str,
    menu_item: MenuItem,
    mongo_ds=Depends(get_mongo_ds)
):
    return RestaurantService.add_menu_item_to_menu(menu_item=menu_item,
                                                   restaurant_id=restaurant_id,
                                                   restaurant_repository=RestaurantRepository(mongo_ds))
                                        