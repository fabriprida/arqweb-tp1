from pydantic import Field
from pydantic import BaseModel 
from schemas.timetable import Timetable

class InputCreateRestaurant(BaseModel):
    name: str = Field(...)
    latitude: str = Field(...)
    longitude: str = Field(...)
    address: str = Field(...)
    phone_number: str = Field(...)
    timetable: Timetable = Field(None) 
    
    