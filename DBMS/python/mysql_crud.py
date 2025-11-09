"""
MySQL DB connectivity example (mysql-connector-python)
Implements basic navigation operations (add, edit, delete, list) on members table.

Prereqs:
- pip install mysql-connector-python
- Create database and table `members` compatible with Oracle schema (or adjust queries).
"""
import os
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "college"),
    )


def add_member(conn, roll_no: str, name: str, email: str):
    sql = (
        "INSERT INTO members(roll_no, name, email, status) "
        "VALUES (%s, %s, %s, 'A')"
    )
    with conn.cursor() as cur:
        cur.execute(sql, (roll_no, name, email))
    conn.commit()


def edit_member_email(conn, roll_no: str, new_email: str):
    sql = "UPDATE members SET email = %s WHERE roll_no = %s"
    with conn.cursor() as cur:
        cur.execute(sql, (new_email, roll_no))
        print(f"Updated rows: {cur.rowcount}")
    conn.commit()


def delete_member(conn, roll_no: str):
    sql = "DELETE FROM members WHERE roll_no = %s"
    with conn.cursor() as cur:
        cur.execute(sql, (roll_no,))
        print(f"Deleted rows: {cur.rowcount}")
    conn.commit()


def list_members(conn):
    sql = "SELECT roll_no, name, email, status FROM members ORDER BY roll_no"
    with conn.cursor() as cur:
        cur.execute(sql)
        for row in cur.fetchall():
            print(row)


def main():
    conn = get_connection()
    try:
        print("Listing members before operations:")
        list_members(conn)

        print("\nAdding member R200...")
        add_member(conn, "R200", "MySQL User", "mysql@example.com")

        print("\nEditing member R200 email...")
        edit_member_email(conn, "R200", "mysql2@example.com")

        print("\nListing members after add/edit:")
        list_members(conn)

        print("\nDeleting member R200...")
        delete_member(conn, "R200")

        print("\nFinal members:")
        list_members(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

