// MongoDB CRUD operations demo (mongosh script)
// Use: mongosh < mongodb/crud_queries.js

use('librarydb');

// Collections: books, members, borrowings
db.books.drop();
db.members.drop();
db.borrowings.drop();

// Inserts (create)
db.members.insertMany([
  { roll_no: 'R001', name: 'Alice', email: 'alice@example.com', status: 'A' },
  { roll_no: 'R002', name: 'Bob', email: 'bob@example.com', status: 'A' },
]);

db.books.insertMany([
  { title: 'Harry Potter and the Philosopher\'s Stone', author: 'J. K. Rowling', category: 'Fantasy', copies: 10 },
  { title: 'A Game of Thrones', author: 'George R. R. Martin', category: 'Fantasy', copies: 8 },
]);

// SAVE method (deprecated but shown per requirement): performs upsert by _id
var doc = { _id: 'B100', title: 'Clean Code', author: 'Robert C. Martin', category: 'Software', copies: 5 };
db.books.save(doc);
// Update same doc using save
doc.copies = 6;
db.books.save(doc);

// Find (read) with logical operators
print('\nBooks in Fantasy OR with copies >= 6:');
db.books.find({ $or: [ { category: 'Fantasy' }, { copies: { $gte: 6 } } ] }).forEach(printjson);

// Update (edit) using $set
db.members.updateOne({ roll_no: 'R002' }, { $set: { email: 'bob+new@example.com' } });

// Delete (remove)
db.books.deleteOne({ title: 'A Game of Thrones' });

// Create borrowing
const alice = db.members.findOne({ roll_no: 'R001' });
const hp = db.books.findOne({ title: /Harry Potter/ });
db.borrowings.insertOne({
  member_id: alice._id,
  book_id: hp._id,
  date_of_issue: new Date(),
  due_date: new Date(Date.now() + 14*24*3600*1000),
  status: 'I'
});

print('\nAll members:');
db.members.find({}).forEach(printjson);

