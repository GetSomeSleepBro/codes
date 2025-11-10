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



# /----------------------------------------------------
# // STEP 1: Switch to Database
# //----------------------------------------------------
# use shopDB
# // switched to db shopDB

# //----------------------------------------------------
# // STEP 2: Create Collection and Insert Sample Data
# //----------------------------------------------------
# db.sales.insertMany([
#   { _id: 1, product: "Pen",      category: "Stationery", price: 10,  quantity: 5,  city: "Pune" },
#   { _id: 2, product: "Book",     category: "Stationery", price: 50,  quantity: 2,  city: "Mumbai" },
#   { _id: 3, product: "Pencil",   category: "Stationery", price: 5,   quantity: 10, city: "Pune" },
#   { _id: 4, product: "Mouse",    category: "Electronics", price: 500, quantity: 1, city: "Pune" },
#   { _id: 5, product: "Keyboard", category: "Electronics", price: 800, quantity: 2, city: "Mumbai" },
#   { _id: 6, product: "Pen",      category: "Stationery", price: 10,  quantity: 3,  city: "Mumbai" },
#   { _id: 7, product: "Mouse",    category: "Electronics", price: 500, quantity: 2,  city: "Pune" }
# ])
# // Output: acknowledged: true, insertedIds: { ... }

# //----------------------------------------------------
# // STEP 3: Create Indexes for Faster Queries
# //----------------------------------------------------
# db.sales.createIndex({ category: 1, city: 1 })  // Compound index on category + city
# db.sales.createIndex({ product: 1 })            // Index on product

# //----------------------------------------------------
# // STEP 4: Check Current Indexes
# //----------------------------------------------------
# db.sales.getIndexes()
# // Output: shows id, category_1_city_1, product_1

# //----------------------------------------------------
# // STEP 5: Aggregation Pipeline Examples
# //----------------------------------------------------

# // 5a. Total sales and total quantity per category per city
# db.sales.aggregate([
#   {
#     $group: {
#       _id: { category: "$category", city: "$city" },
#       total_sales: { $sum: { $multiply: ["$price", "$quantity"] } },
#       total_qty: { $sum: "$quantity" }
#     }
#   },
#   { $sort: { "_id.category": 1, "_id.city": 1 } }
# ])
# // Output: total_sales and total_qty per category/city

# // 5b. Filter Electronics sales in Pune
# db.sales.aggregate([
#   { $match: { category: "Electronics", city: "Pune" } },
#   {
#     $group: {
#       _id: "$product",
#       total_sales: { $sum: { $multiply: ["$price", "$quantity"] } },
#       total_qty: { $sum: "$quantity" }
#     }
#   },
#   { $sort: { total_sales: -1 } }
# ])
# // Output: total sales per product in Electronics/Pune

# // 5c. Projection: Show only product name and total_sales
# db.sales.aggregate([
#   {
#     $group: {
#       _id: "$product",
#       total_sales: { $sum: { $multiply: ["$price", "$quantity"] } }
#     }
#   },
#   { $project: { product: "$_id", total_sales: 1, _id: 0 } }
# ])
# // Output: product name + total_sales only
