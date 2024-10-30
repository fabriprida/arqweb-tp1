from db.datasources.mongo_datasource import MongoDataSource
from db.repositories.restaurant import RestaurantRepository


class RestaurantService:
   def create2(restaurant_id: int, mongo_ds: MongoDataSource):
       
       repo = RestaurantRepository(mongo_ds)
       repo.create_restaurant(restaurant_id)
       return restaurant_id