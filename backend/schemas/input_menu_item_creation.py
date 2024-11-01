from pydantic import BaseModel, Field


class InputMenuItemCreation(BaseModel):
    name: str = Field(..., example="Pizza")
    description: str = Field(..., example="Delicious pizza")
    price: float = Field(..., example=10.99)