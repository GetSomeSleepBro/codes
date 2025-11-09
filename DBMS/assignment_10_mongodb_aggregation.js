use shopDB;
db.sales.insertMany([
  { _id: 1, item: "Laptop",  category: "Electronics", price: 55000, quantity: 3, city: "Pune" },
  { _id: 2, item: "Phone",   category: "Electronics", price: 20000, quantity: 5, city: "Mumbai" },
  { _id: 3, item: "Shoes",   category: "Fashion",     price: 3000,  quantity: 10, city: "Delhi" },
  { _id: 4, item: "Watch",   category: "Fashion",     price: 5000,  quantity: 2, city: "Pune" },
  { _id: 5, item: "TV",      category: "Electronics", price: 40000, quantity: 1, city: "Mumbai" },
  { _id: 6, item: "Bag",     category: "Fashion",     price: 1500,  quantity: 8, city: "Delhi" }
]);
db.sales.aggregate([
  {
    $group: {
      _id: "$category",
      totalSales: { $sum: { $multiply: ["$price", "$quantity"] } },
      totalItems: { $sum: "$quantity" }
    }
  }
]).forEach(printjson);
db.sales.aggregate([
  { $group: { _id: "$city", avgPrice: { $avg: "$price" } } },
  { $sort: { avgPrice: -1 } }
]).forEach(printjson);
db.sales.aggregate([
  {
    $project: {
      _id: 0,
      item: 1,
      city: 1,
      totalValue: { $multiply: ["$price", "$quantity"] }
    }
  }
]).forEach(printjson);
db.sales.createIndex({ category: 1 });
db.sales.createIndex({ category: 1, city: 1 });
db.sales.getIndexes().forEach(printjson);
db.sales.find({ category: "Electronics" }).explain("executionStats");
