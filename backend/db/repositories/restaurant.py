from schemas.input_create_restaurant import InputCreateRestaurant
from db.datasources.mongo_datasource import MongoDataSource

class RestaurantRepository:

    def __init__(self, mongo_datasource: MongoDataSource):
        self._mongo_datasource = mongo_datasource

        self._initialize_collection_names()

    def _initialize_collection_names(self):
        self._restaurants_collection_name = "restaurants"

    def create_restaurant(self, input_create_restaurant: InputCreateRestaurant):
        
        return self._mongo_datasource.insert_one(self._restaurants_collection_name, input_create_restaurant.dict())