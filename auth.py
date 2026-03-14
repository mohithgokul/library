import database


def librarian_login():

    username = input("Username: ")
    password = input("Password: ")

    conn = database.connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM librarians WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        print("Librarian login successful")
        return True
    else:
        print("Invalid librarian credentials")
        return False


def member_login():

    username = input("Username: ")
    password = input("Password: ")

    conn = database.connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT member_id FROM members WHERE username=? AND password=?",
        (username, password)
    )

    member = cursor.fetchone()
    conn.close()

    if member:
        print("Member login successful")
        return member[0]
    else:
        print("Invalid member credentials")
        return None


def register_member():

    name = input("Name: ")
    contact = input("Contact: ")
    username = input("Username: ")
    password = input("Password: ")

    conn = database.connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO members(name, contact, username, password)
    VALUES(?,?,?,?)
    """, (name, contact, username, password))

    conn.commit()
    conn.close()

    print("Member registered successfully")