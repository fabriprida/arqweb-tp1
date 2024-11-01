from typing import List
from db.models.restaurant import Restaurant
from schemas.input_menu_item_creation import InputMenuItemCreation
from schemas.input_list_restaurants import InputListRestaurants
from db.repositories.restaurant import RestaurantRepository
from core.dependencies import get_mongo_ds
from services.restaurant import RestaurantService
from fastapi import APIRouter, status, Query, Depends

from schemas.input_create_restaurant import InputCreateRestaurant

router = APIRouter()

@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=str
)
async def create_restaurant(
    input_create_restaurant: InputCreateRestaurant,
    mongo_ds=Depends(get_mongo_ds)
) -> str:
    return RestaurantService.create_restaurant(input_create_restaurant=input_create_restaurant,
                                               restaurant_repository=RestaurantRepository(mongo_ds))


@router.post(
    "/{restaurant_id}/menu",
    status_code=status.HTTP_201_CREATED,
    response_model=str
)
async def add_menu_item_to_menu(
    restaurant_id: str,
    menu_item: InputMenuItemCreation,
    mongo_ds=Depends(get_mongo_ds)
) -> str:
    return RestaurantService.add_menu_item_to_menu(menu_item=menu_item,
                                                   restaurant_id=restaurant_id,
                                                   restaurant_repository=RestaurantRepository(mongo_ds))

@router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    response_model=List[Restaurant]
)
async def list_restaurants(
    input_list_restaurants: InputListRestaurants = Query(),
    mongo_ds=Depends(get_mongo_ds)
) -> List[Restaurant]:
    
    return RestaurantService.list_restaurants(input_list_restaurants=input_list_restaurants,
                                              restaurant_repository=RestaurantRepository(mongo_ds))