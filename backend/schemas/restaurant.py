from schemas.timetable import Timetable
from pydantic import BaseModel, Field

class Restaurant(BaseModel):
    # !TODO: Create complete DTO
    mongo_id: str = Field(...)
    name: str = Field(...)
    
    latitude: str = Field(...)
    longitude: str = Field(...)
    address: str = Field(...)

    phone_number: str = Field(...)
    email: str = Field(None)
    instagram: str = Field(None)
    
    timetable: Timetable = Field(None) 