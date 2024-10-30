from schemas.input_create_restaurant import InputCreateRestaurant
from db.repositories.restaurant import RestaurantRepository


class RestaurantService:
   
   def create_restaurant(input_create_restaurant: InputCreateRestaurant, restaurant_repository: RestaurantRepository):
       
       return restaurant_repository.create_restaurant(input_create_restaurant)