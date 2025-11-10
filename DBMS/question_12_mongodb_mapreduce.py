import os
from pymongo import MongoClient

# MongoDB map-reduce demo: total marks per age
# Falls back to equivalent aggregation if mapReduce is disabled


def get_collection():
    """Return the collection handle using env vars."""
    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    dbname = os.getenv("MONGODB_DB", "labdb")
    collname = os.getenv("MONGODB_COLL", "students")
    client = MongoClient(uri)
    return client[dbname][collname]


def main():
    """Compute totals per age via mapReduce or aggregation."""
    c = get_collection()
    if c.count_documents({}) == 0:
        c.insert_many([
            {"roll": 1, "name": "Riya", "age": 20, "marks": 82},
            {"roll": 2, "name": "Dev",  "age": 21, "marks": 76},
            {"roll": 3, "name": "Neha", "age": 20, "marks": 91},
            {"roll": 4, "name": "Avi",  "age": 22, "marks": 70},
        ])

    db = c.database
    try:
        res = db.command(
            "mapReduce",
            c.name,
            map="function() { emit(this.age, this.marks); }",
            reduce=(
                "function(key, values) {"
                "  var s = 0; for (var i=0;i<values.length;i++) s += values[i];"
                "  return s;"
                "}"
            ),
            out={"inline": 1},
        )
        print(res.get("results"))
    except Exception as e:
        # Fallback: $group + $sum does the same
        agg = list(c.aggregate([
            {"$group": {"_id": "$age", "total_marks": {"$sum": "$marks"}}},
            {"$sort": {"_id": 1}},
        ]))
        print(agg)


if __name__ == "__main__":
    main()
