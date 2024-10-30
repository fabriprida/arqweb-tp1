from typing import Any, Dict, List, Optional
from pymongo import MongoClien, ASCENDING
from pymongo.errors import ConnectionFailure
from pymongo.database import Database

class MongoDataSource:

    def __init__(self, 
                 host: str = "mongodb", 
                 port: int = 27017, 
                 username: str = None,
                 password: str = None,
                 database: str = None):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._database = database

        self._client: Optional[MongoClient] = None
        self._db: Optional[Database] = None
        self._connect()


    def _connect(self):
        try:
            host = self._host
            port = self._port
            username = self._username
            password = self._password
            self._client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
            self._db = self._client[self._database]
            self._client.admin.command('ping')

        except ConnectionFailure as e:
            print(e)
            raise ConnectionError("Failed to connect to MongoDB")
       
    def close(self):
        if self._client:
            self._client.close()
            self._client = None
            self._db = None

    def get_collection(self, collection_name: str):
        return self._db[collection_name]

    def insert_one(self, collection_name: str, document: dict):
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return str(result.inserted_id)
    
    def find_one(self, collection_name: str, query: dict):
        collection = self.get_collection(collection_name)
        return collection.find_one(query)
    
    def find_many(self, 
                  collection_name: str,
                  query: Dict[str, Any] = {},
                  sort_by: str = "_id",
                  sort_direction: int = ASCENDING,
                  limit: int = 0,
                  skip: int = 0
                  ) -> List[Dict[str, Any]]:
    
        collection = self.get_collection(collection_name)
        cursor = collection.find(query).sort(sort_by, sort_direction).skip(skip).limit(limit)
        return list(cursor)