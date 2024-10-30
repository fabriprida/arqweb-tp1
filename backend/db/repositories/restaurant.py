from db.datasources.mongo_datasource import MongoDataSource


class RestaurantRepository:

    def __init__(self, mongo_datasource: MongoDataSource):
        self._mongo_datasource = mongo_datasource

        self._initialize_collection_names()

    def _initialize_collection_names(self):
        self._restaurants_collection_name = "restaurants"

    def create_restaurant(self, id: int):
        restaurant = {
            "id": id
        }
        return self._mongo_datasource.insert_one(self._restaurants_collection_name, restaurant)