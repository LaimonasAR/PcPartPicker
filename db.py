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
    