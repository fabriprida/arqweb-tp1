from schemas.menu import MenuItem
from schemas.restaurant import Restaurant
from schemas.input_create_restaurant import InputCreateRestaurant
from db.repositories.restaurant import RestaurantRepository


class RestaurantService:
   
    def create_restaurant(input_create_restaurant: InputCreateRestaurant, restaurant_repository: RestaurantRepository):
        
        mongo_id = restaurant_repository.create_restaurant(input_create_restaurant)
       
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
        
    def add_menu_item_to_menu(menu_item: MenuItem, restaurant_id: str, restaurant_repository: RestaurantRepository):
        
        
        