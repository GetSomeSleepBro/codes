"""
MongoDB connectivity example using PyMongo for basic CRUD.

Prereqs:
- pip install pymongo
- MongoDB running locally or update MONGODB_URI
"""
import os
from datetime import datetime, timedelta
from pymongo import MongoClient


def get_client():
    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    return MongoClient(uri)


def add_member(db, roll_no: str, name: str, email: str):
    db.members.insert_one({"roll_no": roll_no, "name": name, "email": email, "status": "A"})


def edit_member_email(db, roll_no: str, new_email: str):
    res = db.members.update_one({"roll_no": roll_no}, {"$set": {"email": new_email}})
    print(f"Matched: {res.matched_count}, Modified: {res.modified_count}")


def delete_member(db, roll_no: str):
    res = db.members.delete_one({"roll_no": roll_no})
    print(f"Deleted: {res.deleted_count}")


def list_members(db):
    for m in db.members.find().sort("roll_no"):
        print(m)


def demo_borrowing(db):
    alice = db.members.find_one({"roll_no": "R001"})
    if not alice:
        add_member(db, "R001", "Alice", "alice@example.com")
        alice = db.members.find_one({"roll_no": "R001"})

    book = db.books.find_one({"title": {"$regex": "Harry Potter"}})
    if not book:
        db.books.insert_one({"title": "Harry Potter and the Philosopher's Stone", "author": "J. K. Rowling", "category": "Fantasy", "copies": 10})
        book = db.books.find_one({"title": {"$regex": "Harry Potter"}})

    db.borrowings.insert_one({
        "member_id": alice["_id"],
        "book_id": book["_id"],
        "date_of_issue": datetime.utcnow(),
        "due_date": datetime.utcnow() + timedelta(days=14),
        "status": "I",
    })


def main():
    client = get_client()
    db = client[os.getenv("MONGODB_DB", "librarydb")]

    print("Members before:")
    list_members(db)

    print("\nAdding member R300...")
    add_member(db, "R300", "Mongo User", "mongo@example.com")
    edit_member_email(db, "R300", "mongo2@example.com")

    print("\nMembers after add/edit:")
    list_members(db)

    print("\nCreating a borrowing demo record...")
    demo_borrowing(db)

    print("\nDeleting member R300...")
    delete_member(db, "R300")

    print("\nFinal members:")
    list_members(db)


if __name__ == "__main__":
    main()

