from typing import List
from schemas.timetable import Timetable
from pydantic import BaseModel, Field

class MenuItem(BaseModel):
    menu_mongo_id: str = Field(..., example="...")
    name: str = Field(..., example="Pizza")
    description: str = Field(..., example="Delicious pizza")
    price: float = Field(..., example=10.99)

class InputMenuItemCreation(BaseModel):
    name: str = Field(..., example="Pizza")
    description: str = Field(..., example="Delicious pizza")
    price: float = Field(..., example=10.99)

example_menu_item = MenuItem(
    menu_mongo_id="123456789",
    name="Pizza",
    description="Delicious pizza",
    price=10.99
)

class Menu(BaseModel):
    mongo_id: str = Field(..., example="...")
    restaurant_id: str = Field(..., example="6722a6e1590f3dd285a31b03")
    items: List[MenuItem] = Field(...,example=[example_menu_item])