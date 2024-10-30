from schemas.menu import InputMenuItemCreation, MenuItem
from schemas.restaurant import Restaurant
from schemas.input_create_restaurant import InputCreateRestaurant
from db.repositories.restaurant import RestaurantRepository


class RestaurantService:
   
    def create_restaurant(input_create_restaurant: InputCreateRestaurant, 
                          restaurant_repository: RestaurantRepository) -> str:
        
        restaurant_mongo_id = restaurant_repository.create_restaurant(input_create_restaurant)
       
        return restaurant_mongo_id
            
         

        
    def add_menu_item_to_menu(menu_item: InputMenuItemCreation, 
                              restaurant_id: str, 
                              restaurant_repository: RestaurantRepository) -> str:
        
        menu_item_mongo_id = restaurant_repository.add_menu_item_to_menu(menu_item, restaurant_id) 
        
        return menu_item_mongo_id