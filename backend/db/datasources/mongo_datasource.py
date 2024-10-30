from typing import Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDataSource:

    def __init__(self, 
                 host: str = "mongodb", 
                 port: int = 27017, 
                 username: str = None,
                 password: str = None):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

        self._client: Optional[MongoClient] = None
        self._connect()


    def _connect(self):
        try:
            host = self._host
            port = self._port
            username = self._username
            password = self._password
            self._client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
            
            self._client.admin.command('ping')

        except ConnectionFailure as e:
            print(e)
            raise ConnectionError("Failed to connect to MongoDB")
       
    def close(self):
        if self._client:
            self._client.close()
            self._client = None

    def insert_one(self, collection_name: str, document: dict):
        result = self._client[collection_name].insert_one(document)
        return str(result.inserted_id)