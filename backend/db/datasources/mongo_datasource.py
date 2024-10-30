from typing import Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDataSource:

    def __init__(self, 
                 host: str = "localhost", 
                 port: int = 27017, 
                 username: str = None,
                 password: str = None,):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

        self._client: Optional[MongoClient] = None
        self._connect()


    def _connect(self):
       try:
            self._client = MongoClient(host=self._host, 
                                       port=self._port,
                                       username=self._username,
                                       password=self._password)
            
            self._client.admin.command("ping")

        except ConnectionFailure:
            raise ConnectionError("Failed to connect to MongoDB")
       

    def insert_one(self, collection_name: str, document: dict):
        result = self._client[collection_name].insert_one(document)
        return str(result.inserted_id)