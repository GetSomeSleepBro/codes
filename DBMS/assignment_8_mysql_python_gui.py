CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
import tkinter as tk
from tkinter import messagebox
import mysql.connector
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # change this
        database="student_db"
    )
def add_record():
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
                (name_var.get(), age_var.get(), course_var.get()))
    con.commit()
    con.close()
    messagebox.showinfo("Success", "Record added successfully!")
    clear_fields()
    view_records()
def view_records():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row)
    con.close()
def delete_record():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    data = listbox.get(selected)
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (data[0],))
    con.commit()
    con.close()
    messagebox.showinfo("Deleted", "Record deleted successfully!")
    view_records()
def edit_record():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to edit")
        return
    data = listbox.get(selected)
    con = connect_db()
    cur = con.cursor()
    cur.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
                (name_var.get(), age_var.get(), course_var.get(), data[0]))
    con.commit()
    con.close()
    messagebox.showinfo("Updated", "Record updated successfully!")
    clear_fields()
    view_records()
def clear_fields():
    name_var.set("")
    age_var.set("")
    course_var.set("")
root = tk.Tk()
root.title("Student Database Navigation")
name_var = tk.StringVar()
age_var = tk.StringVar()
course_var = tk.StringVar()
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1, padx=5, pady=5)
tk.Label(root, text="Course:").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=course_var).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Add", command=add_record).grid(row=3, column=0, pady=10)
tk.Button(root, text="Edit", command=edit_record).grid(row=3, column=1, pady=10)
tk.Button(root, text="Delete", command=delete_record).grid(row=3, column=2, pady=10)
tk.Button(root, text="View All", command=view_records).grid(row=3, column=3, pady=10)
listbox = tk.Listbox(root, width=60)
listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
view_records()
root.mainloop()
