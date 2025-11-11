import os
import sys
import argparse
from pymongo import MongoClient

# Simple MongoDB CLI for books collection
# Commands: add, list, update, delete


def get_collection():
    """Get collection from env vars (MONGODB_URI/DB/COLL)."""
    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    dbname = os.getenv("MONGODB_DB", "labdb")
    collname = os.getenv("MONGODB_COLL", "books")
    client = MongoClient(uri)
    return client[dbname][collname]


def add_book(c, title, author, price):
    """Insert one book document."""
    c.insert_one({"title": title, "author": author, "price": float(price)})


def list_books(c):
    """Print all books (no _id)."""
    for d in c.find({}, {"_id": 0}).sort("title"):
        print(d)


def update_book(c, title, price):
    """Update price for a title (no upsert)."""
    c.update_one({"title": title}, {"$set": {"price": float(price)}}, upsert=False)


def delete_book(c, title):
    """Delete one book by title."""
    c.delete_one({"title": title})


def main():
    p = argparse.ArgumentParser(description="MongoDB books navigation CLI")
    sub = p.add_subparsers(dest="op", required=True)

    a = sub.add_parser("add")
    a.add_argument("title")
    a.add_argument("author")
    a.add_argument("price", type=float)

    sub.add_parser("list")

    u = sub.add_parser("update")
    u.add_argument("title")
    u.add_argument("price", type=float)

    d = sub.add_parser("delete")
    d.add_argument("title")

    args = p.parse_args()
    c = get_collection()

    if args.op == "add":
        add_book(c, args.title, args.author, args.price)
    elif args.op == "list":
        list_books(c)
    elif args.op == "update":
        update_book(c, args.title, args.price)
    elif args.op == "delete":
        delete_book(c, args.title)


if __name__ == "__main__":
    sys.exit(main())



# //----------------------------------------------------
# // MONGOSH EQUIVALENT COMMANDS
# //----------------------------------------------------

# // Switch to the database
# use labdb

# // ADD a new book
# db.books.insertOne({
#   title: "The Great Gatsby",
#   author: "F. Scott Fitzgerald",
#   price: 12.99
# })

# // LIST all books, sorted by title, without the _id field
# db.books.find({}, { _id: 0 }).sort({ title: 1 })

# // UPDATE the price of a book
# db.books.updateOne(
#   { title: "The Great Gatsby" },
#   { $set: { price: 14.99 } }
# )

# // DELETE a book by its title
# db.books.deleteOne({ title: "The Great Gatsby" })
