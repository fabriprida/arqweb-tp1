from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# MongoDB Connection
client = AsyncIOMotorClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client.my_database

# Pydantic Model for our data
class Item(BaseModel):
    name: str
    description: str = None

# Routes
@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    result = await db["items"].insert_one(item.dict())
    if result.inserted_id:
        return {"id": str(result.inserted_id)}
    raise HTTPException(status_code=400, detail="Item creation failed")

@app.get("/items/", response_model=list)
async def read_items():
    items = await db["items"].find().to_list(100)
    return [1, 2, 3, 6]
