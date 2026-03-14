import sqlite3
from datetime import datetime
def connect():
    conn = sqlite3.connect("library.db")
    return conn


def create_tables():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS librarians(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members(
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        contact TEXT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        isbn TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        available INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrow_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        isbn TEXT,
        issue_date TEXT,
        return_date TEXT,
        fine_paid REAL
    )
    """)

    conn.commit()
    conn.close()
def create_default_librarian():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO librarians(username, password)
    VALUES('admin', 'admin123')
    """)

    conn.commit()
    conn.close()

def add_book(title, author, isbn, genre):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books(title, author, isbn, genre, available)
    VALUES(?,?,?,?,1)
    """, (title, author, isbn, genre))

    conn.commit()
    conn.close()
def get_all_books():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    conn.close()

    return books


def issue_book(member_id, isbn):

    conn = connect()
    cursor = conn.cursor()

    # check availability
    cursor.execute("SELECT available FROM books WHERE isbn=?", (isbn,))
    book = cursor.fetchone()

    if not book:
        print("Book not found.")
        conn.close()
        return

    if book[0] == 0:
        print("Book is currently unavailable.")
        conn.close()
        return

    # mark book as issued
    cursor.execute(
        "UPDATE books SET available=0 WHERE isbn=?",
        (isbn,)
    )

    # insert borrow record
    cursor.execute("""
    INSERT INTO borrow_history(member_id, isbn, issue_date)
    VALUES(?,?,?)
    """, (member_id, isbn, datetime.now()))

    conn.commit()
    conn.close()

    print("Book issued successfully.")


def return_book(member_id, isbn):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT issue_date FROM borrow_history
    WHERE member_id=? AND isbn=? AND return_date IS NULL
    """, (member_id, isbn))

    record = cursor.fetchone()

    if not record:
        print("Borrow record not found.")
        conn.close()
        return

    issue_date = datetime.fromisoformat(record[0])
    return_date = datetime.now()

    days = (return_date - issue_date).days

    fine = 0

    if days > 7:
        fine = (days - 7) * 5

    cursor.execute("""
    UPDATE borrow_history
    SET return_date=?, fine_paid=?
    WHERE member_id=? AND isbn=? AND return_date IS NULL
    """, (return_date, fine, member_id, isbn))

    cursor.execute(
        "UPDATE books SET available=1 WHERE isbn=?",
        (isbn,)
    )

    conn.commit()
    conn.close()

    print("Book returned successfully.")

    if fine > 0:
        print(f"Late return fine: ₹{fine}")
# ---------------- REMOVE BOOK ----------------
def remove_book(isbn):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE isbn=?", (isbn,))

    conn.commit()
    conn.close()


# ---------------- UPDATE BOOK ----------------
def update_book(isbn, title, author, genre):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE books
    SET title=?, author=?, genre=?
    WHERE isbn=?
    """, (title, author, genre, isbn))

    conn.commit()
    conn.close()


# ---------------- SEARCH BOOK ----------------
def search_books(keyword):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM books
    WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

    books = cursor.fetchall()

    conn.close()

    return books


# ---------------- MEMBER FUNCTIONS ----------------

def register_member(name, contact, username, password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO members(name, contact, username, password)
    VALUES(?,?,?,?)
    """, (name, contact, username, password))

    conn.commit()
    conn.close()


def get_all_members():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")

    members = cursor.fetchall()

    conn.close()

    return members


def get_member(member_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members WHERE member_id=?", (member_id,))

    member = cursor.fetchone()

    conn.close()

    return member


def remove_member(member_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM members WHERE member_id=?", (member_id,))

    conn.commit()
    conn.close()


def get_member_history(member_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM borrow_history WHERE member_id=?
    """, (member_id,))

    history = cursor.fetchall()

    conn.close()

    return history


def update_member(member_id, contact, password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE members
    SET contact=?, password=?
    WHERE member_id=?
    """, (contact, password, member_id))

    conn.commit()
    conn.close()