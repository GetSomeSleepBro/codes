"""
Oracle DB connectivity example (python-oracledb / cx_Oracle)
Implements basic navigation operations (add, edit, delete, list) on members table.

Prereqs:
- pip install oracledb  (or cx_Oracle)
- Ensure the Oracle schema from sql/oracle_ddl_objects.sql is created.
- Set environment variables or edit DSN values below.
"""
import os

try:
    import oracledb as cx_Oracle  # python-oracledb
except Exception:  # fallback
    import cx_Oracle  # type: ignore


def get_connection():
    user = os.getenv("ORACLE_USER", "user")
    password = os.getenv("ORACLE_PASSWORD", "password")
    dsn = os.getenv("ORACLE_DSN", "localhost/orclpdb1")  # host/service_name
    return cx_Oracle.connect(user=user, password=password, dsn=dsn)


def add_member(conn, roll_no: str, name: str, email: str):
    sql = """
        INSERT INTO members(member_id, roll_no, name, email, status)
        VALUES (seq_members.NEXTVAL, :roll_no, :name, :email, 'A')
    """
    with conn.cursor() as cur:
        cur.execute(sql, roll_no=roll_no, name=name, email=email)
    conn.commit()


def edit_member_email(conn, roll_no: str, new_email: str):
    sql = "UPDATE members SET email = :email WHERE roll_no = :roll_no"
    with conn.cursor() as cur:
        cur.execute(sql, email=new_email, roll_no=roll_no)
        print(f"Updated rows: {cur.rowcount}")
    conn.commit()


def delete_member(conn, roll_no: str):
    sql = "DELETE FROM members WHERE roll_no = :roll_no"
    with conn.cursor() as cur:
        cur.execute(sql, roll_no=roll_no)
        print(f"Deleted rows: {cur.rowcount}")
    conn.commit()


def list_members(conn):
    sql = "SELECT roll_no, name, email, status FROM members ORDER BY roll_no"
    with conn.cursor() as cur:
        for row in cur.execute(sql):
            print(row)


def main():
    conn = get_connection()
    try:
        print("Listing members before operations:")
        list_members(conn)

        print("\nAdding member R100...")
        add_member(conn, "R100", "Test User", "test@example.com")

        print("\nEditing member R100 email...")
        edit_member_email(conn, "R100", "new@example.com")

        print("\nListing members after add/edit:")
        list_members(conn)

        print("\nDeleting member R100...")
        delete_member(conn, "R100")

        print("\nFinal members:")
        list_members(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

