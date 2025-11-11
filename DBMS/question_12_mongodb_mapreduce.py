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


def setup_data(c):
    """Insert sample data if collection is empty."""
    if c.count_documents({}) == 0:
        print("--- Inserting sample documents ---")
        c.insert_many([
            {"roll": 1, "name": "Riya", "age": 20, "marks": 82},
            {"roll": 2, "name": "Dev",  "age": 21, "marks": 76},
            {"roll": 3, "name": "Neha", "age": 20, "marks": 91},
            {"roll": 4, "name": "Avi",  "age": 22, "marks": 70},
        ])
        print("Sample documents inserted.")


def run_map_reduce(c):
    """Compute totals per age via mapReduce."""
    db = c.database
    print("\n--- Running Map-Reduce for total marks per age ---")
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
        print(f"Map-reduce failed: {e}. Trying aggregation fallback.")
        run_aggregation_fallback(c)


def run_aggregation_fallback(c):
    """Compute totals per age via aggregation as a fallback."""
    print("\n--- Running Aggregation for total marks per age (fallback) ---")
    # Fallback: $group + $sum does the same
    agg = list(c.aggregate([
        {"$group": {"_id": "$age", "total_marks": {"$sum": "$marks"}}},
        {"$sort": {"_id": 1}},
    ]))
    print(agg)


def main():
    """Compute totals per age via mapReduce or aggregation."""
    c = get_collection()
    setup_data(c)
    run_map_reduce(c)


if __name__ == "__main__":
    main()



# //----------------------------------------------------
# // STEP 1: Create / Switch to Database
# //----------------------------------------------------
# use shopDB
# // Output: switched to db shopDB


# //----------------------------------------------------
# // STEP 2: Create a Collection and Insert Documents
# //----------------------------------------------------
# // Collection name: sales
# // Each document represents one sales transaction
# db.sales.insertMany([
#   { _id: 1, product: "Pen",    category: "Stationery", price: 10,  quantity: 5 },
#   { _id: 2, product: "Book",   category: "Stationery", price: 50,  quantity: 2 },
#   { _id: 3, product: "Pencil", category: "Stationery", price: 5,   quantity: 10 },
#   { _id: 4, product: "Mouse",  category: "Electronics", price: 500, quantity: 1 },
#   { _id: 5, product: "Keyboard", category: "Electronics", price: 800, quantity: 2 },
#   { _id: 6, product: "Pen",    category: "Stationery", price: 10,  quantity: 3 },
#   { _id: 7, product: "Mouse",  category: "Electronics", price: 500, quantity: 2 }
# ])
# // Output: acknowledged: true


# //----------------------------------------------------
# // STEP 3: Define the MAP Function
# //----------------------------------------------------
# // Emits (key, value) pairs.
# // key   → category
# // value → total amount (price * quantity)
# var mapFunction = function() {
#   emit(this.category, this.price * this.quantity);
# };


# //----------------------------------------------------
# // STEP 4: Define the REDUCE Function
# //----------------------------------------------------
# // Combines all values (total sales amounts) for the same category.
# var reduceFunction = function(keyCategory, values) {
#   return Array.sum(values);   // sum of all sales amounts per category
# };


# //----------------------------------------------------
# // STEP 5: Execute MAP-REDUCE Operation
# //----------------------------------------------------
# // Output collection will store summarized results
# db.sales.mapReduce(
#   mapFunction,
#   reduceFunction,
#   { out: "total_sales" }
# );


# //----------------------------------------------------
# // STEP 6: Display Results
# //----------------------------------------------------
# db.total_sales.find().pretty()
# // Output will show total sales per category


# //----------------------------------------------------
# // END OF MAP-REDUCE PRACTICAL
# //----------------------------------------------------
