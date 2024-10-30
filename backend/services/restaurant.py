from db.datasources.mongo_datasource import MongoDataSource
from db.repositories.restaurant import RestaurantRepository


class RestaurantService:
   def create2(restaurant_id):
       
       mongo_ds = MongoDataSource(host="localhost", port=27017, username="admin", password="password")
       repo = RestaurantRepository(mongo_ds)
       repo.create_restaurant(restaurant_id)
       return restaurant_id