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



# //----------------------------------------------------
# // STEP 1: Create or Switch to Database
# //----------------------------------------------------
# use studentDB
# // Output: switched to db studentDB


# //----------------------------------------------------
# // STEP 2: Create Collection and Insert Documents (CREATE)
# //----------------------------------------------------
# // insertMany() adds multiple records to the collection
# db.students.insertMany([
#   { _id: 1, name: "Asmita", branch: "Computer", marks: 85, city: "Pune" },
#   { _id: 2, name: "Riya", branch: "ENTC", marks: 65, city: "Mumbai" },
#   { _id: 3, name: "Sahil", branch: "Computer", marks: 55, city: "Nashik" },
#   { _id: 4, name: "Amit", branch: "IT", marks: 90, city: "Pune" },
#   { _id: 5, name: "Pooja", branch: "ENTC", marks: 40, city: "Kolhapur" }
# ])
# // Output: acknowledged: true, insertedIds: ...


# //----------------------------------------------------
# // STEP 3: Display All Documents (READ)
# //----------------------------------------------------
# db.students.find().pretty()
# // .pretty() displays documents in a readable format


# //----------------------------------------------------
# // STEP 4: Use Comparison Operators ($gt, $lt)
# //----------------------------------------------------
# // Display students with marks greater than 60
# db.students.find({ marks: { $gt: 60 } })

# // Display students with marks less than 60
# db.students.find({ marks: { $lt: 60 } })


# //----------------------------------------------------
# // STEP 5: Use Logical Operators ($or, $and)
# //----------------------------------------------------
# // Display students from Pune OR Mumbai
# db.students.find({
#   $or: [ { city: "Pune" }, { city: "Mumbai" } ]
# })

# // Display Computer branch students having marks greater than 70
# db.students.find({
#   $and: [ { branch: "Computer" }, { marks: { $gt: 70 } } ]
# })


# //----------------------------------------------------
# // STEP 6: Update Operations (UPDATE)
# //----------------------------------------------------
# // Update one student's marks using updateOne()
# db.students.updateOne(
#   { name: "Pooja" },
#   { $set: { marks: 60 } }
# )
# // $set updates only the mentioned field


# // Update all ENTC students to "Electronics & Telecom"
# db.students.updateMany(
#   { branch: "ENTC" },
#   { $set: { branch: "Electronics & Telecom" } }
# )


# //----------------------------------------------------
# // STEP 7: Use SAVE Method (INSERT or UPDATE)
# //----------------------------------------------------
# // save() inserts a new record if _id doesn’t exist,
# // or updates the record if _id already exists.
# db.students.save({
#   _id: 6,
#   name: "Neha",
#   branch: "Computer",
#   marks: 78,
#   city: "Pune"
# })


# //----------------------------------------------------
# // STEP 8: Delete Operations (DELETE)
# //----------------------------------------------------
# // Delete a specific student by name
# db.students.deleteOne({ name: "Sahil" })

# // Delete all students having marks less than 50
# db.students.deleteMany({ marks: { $lt: 50 } })


# //----------------------------------------------------
# // STEP 9: Display Final Collection Data
# //----------------------------------------------------
# db.students.find().pretty()


# //----------------------------------------------------
# // STEP 10: Display with Sorting and Projection (Optional)
# //----------------------------------------------------
# // Sort students by marks in descending order
# db.students.find().sort({ marks: -1 })

# // Display only name and marks fields (projection)
# db.students.find({}, { name: 1, marks: 1, _id: 0 })


# //----------------------------------------------------
# // END OF CRUD PRACTICAL
# //----------------------------------------------------
