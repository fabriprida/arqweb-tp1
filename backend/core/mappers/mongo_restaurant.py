from db.models.restaurant import Restaurant


def map_mongo_to_restaurant_model(mongo_restaurant: dict) -> Restaurant:
    return Restaurant(
        mongo_id=mongo_restaurant["_id"],
        name=mongo_restaurant["name"],
        latitude=mongo_restaurant["latitude"],
        longitude=mongo_restaurant["longitude"],
        address=mongo_restaurant["address"],
        phone_number=mongo_restaurant["phone_number"],
        email=mongo_restaurant.get("email"),
        instagram=mongo_restaurant.get("instagram"),
        timetable=map_mongo_to_timetable_model(mongo_restaurant.get("timetable"))
    )
