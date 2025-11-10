import os
from pymongo import MongoClient

# MongoDB CRUD demo on a 'students' collection
# Shows insert/find/update/delete and logical operators


def get_collection():
    """Return the target Mongo collection using env vars."""
    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    dbname = os.getenv("MONGODB_DB", "labdb")
    collname = os.getenv("MONGODB_COLL", "students")
    client = MongoClient(uri)
    return client[dbname][collname]


def main():
    """Run simple CRUD operations."""
    c = get_collection()

    c.delete_many({})  # clean slate for demo

    c.insert_one({"roll": 1, "name": "Riya", "age": 20, "marks": 82})
    c.insert_many([
        {"roll": 2, "name": "Dev",  "age": 21, "marks": 76},
        {"roll": 3, "name": "Neha", "age": 20, "marks": 91},
    ])

    # Use $or and $gte to filter
    for d in c.find({"$or": [{"age": 20}, {"marks": {"$gte": 90}}]}).sort("roll"):
        print(d)

    c.update_one({"roll": 2}, {"$set": {"marks": 80}})  # partial update

    c.replace_one({"roll": 4}, {"roll": 4, "name": "Avi", "age": 22, "marks": 70}, upsert=True)  # full replace

    c.delete_one({"roll": 1})  # single delete

    print(list(c.find({}, {"_id": 0}).sort("roll")))


if __name__ == "__main__":
    main()
