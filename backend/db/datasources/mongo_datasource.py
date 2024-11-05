from typing import Any, Dict, List, Optional
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
from pymongo.database import Database

class MongoDataSource:

    def __init__(self, connection_string: str, database: str):
        self._connection_string = connection_string
        self._database = database

        self._client: Optional[MongoClient] = None
        self._db: Optional[Database] = None
        self._connect()


    def _connect(self):
        try:
            self._client = MongoClient(self._connection_string)
            self._db = self._client[self._database]
            self._client.admin.command('ping')
            print("Connected to MongoDB")
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Connected to MongoDB")

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
    
    def update_one(self, collection_name: str, query: Dict[str, Any], update: Dict[str, Any]):
        collection = self.get_collection(collection_name)
        result = collection.update_one(query, update)
        return result.modified_count

    def find_one(self, collection_name: str, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Find a single document in a collection."""
        collection = self.get_collection(collection_name)
        return collection.find_one(query)


    def aggregate(self, collection_name: str, pipeline: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Perform an aggregation operation on a collection.

        Args:
            collection_name (str): Name of the collection to aggregate.
            pipeline (List[Dict[str, Any]]): The aggregation pipeline to execute.

        Returns:
            List[Dict[str, Any]]: The result of the aggregation operation.
        """
        collection = self.get_collection(collection_name)
        try:
            result = list(collection.aggregate(pipeline))
            return result
        except Exception as e:
            raise Exception(f"Aggregation failed: {str(e)}")


    def find_many(self,
                collection_name: str,
                query: Dict[str, Any] = {},
                sort_by: str = '_id',
                sort_direction: int = ASCENDING,
                limit: int = 0,
                skip: int = 0) -> List[Dict[str, Any]]:
        """
        Find multiple documents in a collection with filtering and pagination.

        Args:
            collection_name (str): Name of the collection to query.
            query (Dict[str, Any], optional): Query filter. Defaults to {}.
            sort_by (str, optional): Field to sort by. Defaults to '_id'.
            sort_direction (int, optional): Sort direction (ASCENDING or DESCENDING). Defaults to ASCENDING.
            limit (int, optional): Maximum number of documents to return. Defaults to 10.
            skip (int, optional): Number of documents to skip. Defaults to 0.

        Returns:
            List[Dict[str, Any]]: List of documents matching the query and pagination parameters.
        """
        collection = self.get_collection(collection_name)
        cursor = collection.find(query)
        cursor = cursor.sort(sort_by, sort_direction)
        cursor = cursor.skip(skip).limit(limit)
        return list(cursor)


    def distinct(self, distinct_column: str, collection_name: str, sort: int = 0):
        pipeline = [
            {"$group": {"_id": f"${distinct_column}"}},
            {"$sort": {"_id": sort}}
        ]
        fields = self.aggregate(collection_name, pipeline)
        return [field["_id"] for field in fields]
