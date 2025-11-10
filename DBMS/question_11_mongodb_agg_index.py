import os
from pymongo import MongoClient, ASCENDING, DESCENDING

# MongoDB indexing + aggregation
# - Create indexes to speed queries
# - Use $group and $sort to summarize data


def get_collection():
    """Return the collection handle using env vars."""
    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    dbname = os.getenv("MONGODB_DB", "labdb")
    collname = os.getenv("MONGODB_COLL", "students")
    client = MongoClient(uri)
    return client[dbname][collname]


def main():
    """Create indexes and run aggregation pipelines."""
    c = get_collection()

    # Indexes: unique roll, and supporting lookups on age/marks
    c.create_index([("roll", ASCENDING)], unique=True)
    c.create_index([("age", ASCENDING)])
    c.create_index([("marks", DESCENDING)])

    if c.count_documents({}) == 0:
        c.insert_many([
            {"roll": 1, "name": "Riya", "age": 20, "marks": 82},
            {"roll": 2, "name": "Dev",  "age": 21, "marks": 76},
            {"roll": 3, "name": "Neha", "age": 20, "marks": 91},
            {"roll": 4, "name": "Avi",  "age": 22, "marks": 70},
        ])

    # Average marks per age
    pipeline = [
        {"$group": {"_id": "$age", "avg_marks": {"$avg": "$marks"}, "count": {"$sum": 1}}},
        {"$sort": {"avg_marks": -1}},
    ]
    for d in c.aggregate(pipeline):
        print(d)

    # Top scorer
    top = list(c.aggregate([
        {"$sort": {"marks": -1}},
        {"$limit": 1},
        {"$project": {"_id": 0, "roll": 1, "name": 1, "marks": 1}},
    ]))
    print(top)


if __name__ == "__main__":
    main()
