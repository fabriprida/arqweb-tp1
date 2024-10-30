from pydantic import Field
from pydantic import BaseModel 
from schemas.timetable import Timetable

class InputCreateRestaurant(BaseModel):
    name: str = Field(..., example="Güerrín")
    
    latitude: str = Field(..., example="-34.6036844")
    longitude: str = Field(..., example="-58.3815591")
    address: str = Field(..., example="Av. Corrientes 1368")

    phone_number: str = Field(..., example="011 4371-8141")
    email: str = Field(None, example="guerrin@gmail.com")
    instagram: str = Field(None, example="guerrinoficial")
    
    timetable: Timetable = Field(None) 
    
    