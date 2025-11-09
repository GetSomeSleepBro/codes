// MongoDB Aggregation and Indexing demo
// Use: mongosh < mongodb/aggregation_indexing.js

use('librarydb');

// Indexing
db.books.createIndex({ title: 1 }, { name: 'idx_books_title' });
db.members.createIndex({ roll_no: 1 }, { unique: true, name: 'ux_members_roll' });
db.borrowings.createIndex({ member_id: 1, book_id: 1 }, { name: 'idx_borrow_member_book' });

// Aggregation: Top borrowed books
print('\nTop borrowed books:');
db.borrowings.aggregate([
  { $group: { _id: "$book_id", borrow_count: { $sum: 1 } } },
  { $sort: { borrow_count: -1 } },
  { $limit: 5 },
  { $lookup: {
      from: 'books',
      localField: '_id',
      foreignField: '_id',
      as: 'book'
  }},
  { $unwind: '$book' },
  { $project: { _id: 0, title: '$book.title', borrow_count: 1 } }
]).forEach(printjson);

// Aggregation: Current borrowings with member and book names
print('\nCurrent borrowings with member/book:');
db.borrowings.aggregate([
  { $match: { status: 'I' } },
  { $lookup: { from: 'members', localField: 'member_id', foreignField: '_id', as: 'm' } },
  { $lookup: { from: 'books', localField: 'book_id', foreignField: '_id', as: 'b' } },
  { $unwind: '$m' },
  { $unwind: '$b' },
  { $project: { _id: 0, member: '$m.name', title: '$b.title', due_date: 1 } }
]).forEach(printjson);

