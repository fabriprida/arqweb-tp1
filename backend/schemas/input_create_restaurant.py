from pydantic import Field, BaseModel 
from schemas.timetable import Timetable

example_timetable = Timetable(timetable={"Monday": [{"opening_time": "12:00", "closing_time": "20:00"}],
                                "Tuesday": [{"opening_time": "13:00", "closing_time": "19:00"}],
                                "Thursday": [{"opening_time": "08:00", "closing_time": "15:00"},
                                            {"opening_time": "16:00", "closing_time": "20:00"}],
                                "Friday": [{"opening_time": "08:00", "closing_time": "20:00"}],
                                "Saturday": [{"opening_time": "08:00", "closing_time": "20:00"}],
                                "Sunday": [{"opening_time": "08:00", "closing_time": "20:00"}]})

class InputCreateRestaurant(BaseModel):
    name: str = Field(..., example="Güerrín")
    
    latitude: str = Field(..., example="-34.6036844")
    longitude: str = Field(..., example="-58.3815591")
    address: str = Field(..., example="Av. Corrientes 1368")

    phone_number: str = Field(..., example="011 4371-8141")
    email: str = Field(None, example="guerrin@gmail.com")
    instagram: str = Field(None, example="guerrinoficial")
    
    timetable: Timetable = Field(None, example=example_timetable) 
    

    