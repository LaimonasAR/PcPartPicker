from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from col_data import parts_data


class PartsDb:
    def __init__(self, host: str, port: int, db_name: str, collection: str) -> None:
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection = collection

    def connect_to_mongodb(self) -> Database:
        client = MongoClient(self.host, self.port)
        database = client[self.db_name]
        return database

    def create(self, document: dict) -> str:
        db = self.connect_to_mongodb()
        collection = db[self.collection]
        result = collection.insert_one(document)
        return f"Inserted document with ID: {result.inserted_id}"


db_task = PartsDb(host="0.0.0.0", port=27017, db_name="PcParts", collection="warehouse")

for sale in parts_data:
    db_task.create(document=sale)
