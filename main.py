import database
import auth
from library import Library

database.create_tables()
database.create_default_librarian()

library = Library()

while True:

    print("\n===== LIBRARY SYSTEM =====")
    print("1. Librarian Login")
    print("2. Member Login")
    print("3. Register as Member")
    print("0. Exit")

    role = input("Select option: ")

    # ---------------- LIBRARIAN LOGIN ---------------- #
    if role == "1":

        if not auth.librarian_login():
            continue

        while True:

            print("\n===== LIBRARIAN MENU =====")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Update Book")
            print("4. Display Books")
            print("5. Recommend Books")
            print("6. Add Member")
            print("7. View All Members")
            print("8. View Member Details")
            print("9. Remove Member")
            print("0. Logout")

            choice = input("Choice: ")

            if choice == "1":

                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                genre = input("Genre: ")

                library.add_book(title, author, isbn, genre)

            elif choice == "2":

                isbn = input("ISBN: ")
                library.remove_book(isbn)

            elif choice == "3":

                isbn = input("ISBN: ")
                title = input("Title: ")
                author = input("Author: ")
                genre = input("Genre: ")

                library.update_book(isbn, title, author, genre)

            elif choice == "4":

                library.display_books()

            elif choice == "5":

                isbn = input("ISBN: ")
                library.recommend_books(isbn)

            elif choice == "6":

                name = input("Name: ")
                contact = input("Contact: ")
                username = input("Username: ")
                password = input("Password: ")

                library.add_member(name, contact, username, password)

            elif choice == "7":

                library.list_members()

            elif choice == "8":

                member_id = input("Member ID: ")
                library.view_member(member_id)

            elif choice == "9":

                member_id = input("Member ID: ")
                library.remove_member(member_id)

            elif choice == "0":
                break

    # ---------------- MEMBER LOGIN ---------------- #
    elif role == "2":

        member_id = auth.member_login()

        if not member_id:
            continue

        while True:

            print("\n===== MEMBER MENU =====")
            print("1. Issue Book")
            print("2. Return Book")
            print("3. Display Books")
            print("4. Recommend Books")
            print("5. Update Contact/Password")
            print("0. Logout")

            choice = input("Choice: ")

            if choice == "1":

                isbn = input("ISBN: ")
                library.issue_book(member_id, isbn)

            elif choice == "2":

                isbn = input("ISBN: ")
                library.return_book(member_id, isbn)

            elif choice == "3":

                library.display_books()

            elif choice == "4":

                isbn = input("ISBN: ")
                library.recommend_books(isbn)

            elif choice == "5":

                library.update_member_details(member_id)

            elif choice == "0":
                break

    # ---------------- REGISTER MEMBER ---------------- #
    elif role == "3":

        auth.register_member()

    elif role == "0":
        print("Exiting system")
        break