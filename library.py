import pandas as pd
import database
from recommender import BookRecommender
from datetime import datetime


class Library:

    # ---------------- BOOK DATAFRAME FOR ML ---------------- #
    def get_books_dataframe(self):

        books = database.get_all_books()

        data = []

        for b in books:
            data.append({
                "isbn": b[0],
                "title": b[1],
                "author": b[2],
                "genre": b[3]
            })

        return pd.DataFrame(data)


    # ---------------- ADD BOOK ---------------- #
    def add_book(self, title, author, isbn, genre):

        database.add_book(title, author, isbn, genre)
        print("Book added successfully.")


    # ---------------- REMOVE BOOK ---------------- #
    def remove_book(self, isbn):

        database.remove_book(isbn)
        print("Book removed successfully.")


    # ---------------- UPDATE BOOK ---------------- #
    def update_book(self, isbn, title, author, genre):

        database.update_book(isbn, title, author, genre)
        print("Book updated successfully.")


    # ---------------- DISPLAY BOOKS ---------------- #
    def display_books(self):

        books = database.get_all_books()

        if not books:
            print("No books found")
            return

        print("\n===== BOOK LIST =====")

        for book in books:

            isbn = book[0]
            title = book[1]
            author = book[2]
            genre = book[3]
            available = book[4]

            status = "Available" if available == 1 else "Issued"

            print(f"{title} | {author} | ISBN: {isbn} | {genre} | {status}")


    # ---------------- SEARCH BOOK ---------------- #
    def search_book(self, keyword):

        books = database.search_books(keyword)

        if not books:
            print("No matching book found")
            return

        for b in books:
            print(f"{b[1]} | {b[2]} | ISBN: {b[0]} | {b[3]}")


    # ---------------- BOOK RECOMMENDATION ---------------- #
    def recommend_books(self, isbn):

        df = self.get_books_dataframe()

        if len(df) < 2:
            print("Not enough books for recommendation")
            return

        recommender = BookRecommender(df)

        recommendations = recommender.recommend(isbn)

        if not recommendations:
            print("No recommendations found")
            return

        print("\nRecommended Books:")

        for r in recommendations:
            print("-", r)


    # ---------------- REGISTER MEMBER ---------------- #
    def register_member(self, name, contact, username, password):

        database.register_member(name, contact, username, password)

        print("Member registered successfully.")


    # ---------------- ADD MEMBER (LIBRARIAN) ---------------- #
    def add_member(self, name, contact, username, password):

        database.register_member(name, contact, username, password)

        print("Member added successfully.")


    # ---------------- REMOVE MEMBER ---------------- #
    def remove_member(self, member_id):

        database.remove_member(member_id)

        print("Member removed successfully.")


    # ---------------- VIEW ALL MEMBERS ---------------- #
    def list_members(self):

        members = database.get_all_members()

        if not members:
            print("No members found")
            return

        print("\n===== MEMBER LIST =====")

        for m in members:
            print(f"ID: {m[0]} | Name: {m[1]} | Contact: {m[2]} | Username: {m[3]}")


    # ---------------- VIEW MEMBER DETAILS ---------------- #
    def view_member(self, member_id):

        member = database.get_member(member_id)

        if not member:
            print("Member not found")
            return

        print(f"\nMember ID: {member[0]}")
        print(f"Name: {member[1]}")
        print(f"Contact: {member[2]}")
        print(f"Username: {member[3]}")

        history = database.get_member_history(member_id)

        if not history:
            print("No borrow history")
            return

        print("\nBorrow History:")

        for h in history:

            isbn = h[2]
            issue_date = h[3]
            return_date = h[4]
            fine = h[5]

            print(f"Book ISBN: {isbn} | Issued: {issue_date} | Returned: {return_date} | Fine: {fine}")

    def update_member_details(self, member_id):

        contact = input("New Contact: ")
        password = input("New Password: ")

        database.update_member(member_id, contact, password)

        print("Member details updated successfully")
    # ---------------- ISSUE BOOK ---------------- #
    def issue_book(self, member_id, isbn):

        database.issue_book(member_id, isbn)


    # ---------------- RETURN BOOK ---------------- #
    def return_book(self, member_id, isbn):

        database.return_book(member_id, isbn)