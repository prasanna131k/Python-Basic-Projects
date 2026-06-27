
from datetime import datetime, timedelta

# Master Dictionary
library = {}


# Function to add a new book
def add_book():
    isbn = input("Enter ISBN Number: ")

    if isbn in library:
        print("Book with this ISBN already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    }

    print("Book Added Successfully!")


# Function to calculate due date
def check_due_date(issue_date):
    due_date = issue_date + timedelta(days=7)
    return due_date.strftime("%d-%m-%Y")


# Function to issue a book
def issue_book():
    isbn = input("Enter ISBN: ")

    if isbn not in library:
        print("Book not found!")
        return

    if not library[isbn]["available"]:
        print("Book is already issued!")
        return

    student_id = input("Enter Borrower ID: ")
    borrower = input("Enter Your Name: ")

    issue_date = datetime.now()

    library[isbn]["available"] = False
    library[isbn]["borrower"] = borrower
    library[isbn]["student_id"] = student_id
    library[isbn]["issue_date"] = issue_date

    print("\nBook Issued Successfully!")
    print("Title :", library[isbn]["title"])
    print("Due Date :", check_due_date(issue_date))


# Function to return a book
def return_book():
    isbn = input("Enter ISBN: ")

    if isbn not in library:
        print("Book not found!")
        return

    if library[isbn]["available"]:
        print("This book is already available in library!")
        return

    library[isbn]["available"] = True
    library[isbn]["borrower"] = None
    library[isbn]["student_id"] = None
    library[isbn]["issue_date"] = None

    print("Book Returned Successfully!")


# Function to search books
def search_book():
    keyword = input("Enter Title or Author Name: ").lower()

    found = False

    for isbn, book in library.items():
        if (keyword in book["title"].lower() or
                keyword in book["author"].lower()):

            found = True

            print("\nISBN :", isbn)
            print("Title :", book["title"])
            print("Author :", book["author"])

            if book["available"]:
                print("Status : Available")
            else:
                print("Status : Issued")

    if not found:
        print("No book found!")


# Function to display all books
def view_catalog():
    if len(library) == 0:
        print("Library is Empty!")
        return

    print("\n------ LIBRARY CATALOG ------")

    for isbn, book in library.items():
        print("\nISBN :", isbn)
        print("Title :", book["title"])
        print("Author :", book["author"])

        if book["available"]:
            print("Status : Available")
        else:
            print("Status : Issued")
            print("Borrower :", book["borrower"])
            print("Student ID :", book["student_id"])
            print("Issue Date :",
                  book["issue_date"].strftime("%d-%m-%Y"))





while True:
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            issue_book()

        elif choice == 3:
            return_book()

        elif choice == 4:
            search_book()

        elif choice == 5:
            view_catalog()

        elif choice == 6:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please Enter Numbers Only!")