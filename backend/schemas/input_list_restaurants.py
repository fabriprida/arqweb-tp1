from pydantic import Field, BaseModel 

class InputListRestaurants(BaseModel):
    
    name: str = Field(None, example="Güerrín")
    restaurant_mongo_id: str = Field(None, example="5f4b6b3b9b3f4b3b9b3f4b3b")
    

    