from pydantic import Field
from pydantic import BaseModel 

# Pydantic Model for our data
class InputCreateRestaurant(BaseModel):
    name: str = Field(...)
    latitude: str = Field(...)
    longitude: str = Field(...)
    
    