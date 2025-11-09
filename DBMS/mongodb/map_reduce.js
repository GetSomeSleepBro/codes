// MongoDB Map-Reduce demo: Count borrowings per category
// Use: mongosh < mongodb/map_reduce.js

use('librarydb');

// Map: emit category with count 1 for each borrowing
var mapFn = function () {
  emit(this.category || 'Unknown', 1);
};

// Reduce: sum counts
var reduceFn = function (key, values) {
  return Array.sum(values);
};

// Prepare a borrowing_by_category view-like collection (denormalized for demo)
db.borrowings_by_category?.drop?.();
db.borrowings.aggregate([
  { $lookup: { from: 'books', localField: 'book_id', foreignField: '_id', as: 'b' } },
  { $unwind: '$b' },
  { $project: { category: '$b.category' } },
  { $out: 'borrowings_by_category' }
]);

// Run mapReduce
db.borrowings_by_category.mapReduce(mapFn, reduceFn, { out: 'mr_borrow_count_by_category' });

print('\nMapReduce results:');
db.mr_borrow_count_by_category.find().forEach(printjson);

