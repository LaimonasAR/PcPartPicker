from db import Mongo

mongodb_host = "0.0.0.0"
mongodb_port = 27017
database_name = "PcParts"
collection_name = "warehouse"

my_db = Mongo(
    host=mongodb_host, port=mongodb_port, db_name=database_name, coll=collection_name
)


def find_part(query: dict) -> list:
    found = my_db.find_parts(query=query)
    return found


def create_part(task: dict) -> str:
    creation = my_db.create_part(task)
    return creation


def update_part(query: dict, update: dict) -> str:
    updated = my_db.update_part(query=query, update=update)
    return updated


def delete_part(query: dict) -> str:
    deleted = my_db.delete_part(query=query)
    return deleted
