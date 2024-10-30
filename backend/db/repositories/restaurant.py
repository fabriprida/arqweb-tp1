from schemas.menu import InputMenuItemCreation
from schemas.input_create_restaurant import InputCreateRestaurant
from db.datasources.mongo_datasource import MongoDataSource

class RestaurantRepository:

    def __init__(self, mongo_datasource: MongoDataSource):
        self._mongo_datasource = mongo_datasource

        self._initialize_collection_names()

    def _initialize_collection_names(self):
        self._restaurants_collection_name = "restaurants"
        self._menus_collection_name = "menus"

    def create_restaurant(self, input_create_restaurant: InputCreateRestaurant) -> str:
        
        return self._mongo_datasource.insert_one(collection_name=self._restaurants_collection_name, 
                                                 document=input_create_restaurant.dict())
    
    def add_menu_item_to_menu(self, 
                              menu_item: InputMenuItemCreation, 
                              restaurant_id: str) -> str:
        
        menu_item_document = menu_item.dict()
        menu_ids = self.get_menu_id(restaurant_id=restaurant_id)
        
        menu_item_document["menu_ids"] = menu_ids
        
        
        return self._mongo_datasource.insert_one(collection_name=self._menus_collection_name,
                                                 document=menu_item_document)
        