from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List


class Mongo:
    def __init__(self, host: str, port: int, db_name: str, coll: str) -> None:
        self.host = host
        self.port = port
        self.db_name = db_name
        self.coll = coll

    def connect_to_mongodb(self) -> Database:
        client = MongoClient(self.host, self.port)
        database = client[self.db_name]
        return database

    def find_parts(self, query: dict) -> List[Dict]:
        db = self.connect_to_mongodb()
        collection = db[self.coll]
        parts = collection.find(query)
        return list(parts)

    def create_part(self, document: dict) -> str:
        db = self.connect_to_mongodb()
        collection = db[self.coll]
        result = collection.insert_one(document)
        return f"Inserted document with ID: {result.inserted_id}"

    def update_part(self, query: Dict, update: Dict) -> int:
        db = self.connect_to_mongodb()
        collection = db[self.coll]
        result = collection.update_many(query, {"$set": update})
        return f"Modified {result.modified_count} parts"

    def delete_part(self, query: Dict) -> int:
        db = self.connect_to_mongodb()
        collection = db[self.coll]
        result = collection.delete_many(query)
        return f"Deleted {result.deleted_count} parts"
