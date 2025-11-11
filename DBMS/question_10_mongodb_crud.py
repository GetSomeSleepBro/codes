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


def create_documents(c):
    """Insert initial documents into the collection."""
    print("--- Inserting documents ---")
    c.insert_one({"roll": 1, "name": "Riya", "age": 20, "marks": 82})
    c.insert_many([
        {"roll": 2, "name": "Dev",  "age": 21, "marks": 76},
        {"roll": 3, "name": "Neha", "age": 20, "marks": 91},
    ])
    print("Documents inserted.")


def read_documents(c):
    """Find and print documents using a filter."""
    print("\n--- Reading documents (age=20 or marks>=90) ---")
    # Use $or and $gte to filter
    for d in c.find({"$or": [{"age": 20}, {"marks": {"$gte": 90}}]}).sort("roll"):
        print(d)


def update_documents(c):
    """Update and replace documents in the collection."""
    print("\n--- Updating documents ---")
    # Partial update using $set
    c.update_one({"roll": 2}, {"$set": {"marks": 80}})
    print("Updated roll 2.")

    # Full replace with upsert
    c.replace_one({"roll": 4}, {"roll": 4, "name": "Avi", "age": 22, "marks": 70}, upsert=True)
    print("Replaced/upserted roll 4.")


def delete_documents(c):
    """Delete a document from the collection."""
    print("\n--- Deleting a document ---")
    c.delete_one({"roll": 1})
    print("Deleted roll 1.")


def list_all_documents(c):
    """List all documents in the collection, sorted by roll."""
    print("\n--- Final documents in collection ---")
    print(list(c.find({}, {"_id": 0}).sort("roll")))


def main():
    """Run simple CRUD operations."""
    c = get_collection()

    # Clean slate for the demo
    c.delete_many({})
    print("Cleared the collection.")

    create_documents(c)
    read_documents(c)
    update_documents(c)
    delete_documents(c)
    list_all_documents(c)


if __name__ == "__main__":
    main()
