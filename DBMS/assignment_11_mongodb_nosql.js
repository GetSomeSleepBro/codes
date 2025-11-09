use collegeDB;
db.students.insertMany([
  { rollno: 101, name: "Amit",   course: "BCA", marks: 85 },
  { rollno: 102, name: "Sneha",  course: "BBA", marks: 78 },
  { rollno: 103, name: "Rahul",  course: "BCA", marks: 90 },
  { rollno: 104, name: "Priya",  course: "BSc", marks: 70 }
]);
db.students.find().forEach(printjson);
db.students.find({ course: "BCA" }).forEach(printjson);
db.students.insertOne({ rollno: 105, name: "Kiran", course: "BBA", marks: 82 });
db.students.updateOne(
  { rollno: 104 },
  { $set: { marks: 75 } }
);
db.students.deleteOne({ rollno: 102 });
db.students.find().forEach(printjson);
