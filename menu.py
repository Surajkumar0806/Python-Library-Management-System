from library import Library
from validation import *
from book import Book
from member_library import Member_library





def menu(library):    
        print(
        "1. Add Book\n"
        "2. Borrow Book\n"
        "3. Return Book\n"
        "4. Search Book\n"
        "5. Display All Books\n"
        "6. Add member\n"
        "7. Search member\n"
        "8. Display all members\n"
        "0. Exit\n")

def add_book_menu(library):
    book_id=total_copies_validation("Enter the book ID")
    title=text_validation("Enter title of the book: ")
    author=text_validation("Enter Author name: ")
    section=text_validation("What seection does the book belong to: ")
    total_copies=total_copies_validation("Enter total copies of book")
    book=Book(book_id, title, author, section, total_copies)
    added= library.add_book(book)
    library.save_to_json()
    if added:
        print("Book added sucessfully ")
    else:
        print("Book already exsist total copies increased")
    
def borrow_book_menu(library, member_library):
    member_id=total_copies_validation("Enter Member ID: ")
    get_member=member_library.find_member_by_id(member_id)
    if get_member is None: 
        print("Member not found")
        return
    if get_member.get_borrowed_count() >= 5:
        print("Maximum borrow limit reached")
        return
    book_id=total_copies_validation("Enter book ID: ")
    borrow=library.borrow_book(book_id)
    member_borrow=member_library.borrow_book_member(member_id, book_id)
    library.save_to_json()
    member_library.save_member_to_json()
    if borrow and member_borrow:
        print("Enjoy the book")
    elif borrow is None:
        print("Book not found")
    elif not member_borrow:
        print("Can not allow to borrow the same book")
    else:
        print("No copies available")

def return_book_menu(library, member_library):
    member_id=total_copies_validation("Enter Member ID: ")
    book_id=total_copies_validation("Enter book ID: ")
    returning=library.return_book(book_id)
    member_returning=member_library.return_book(member_id, book_id)
    library.save_to_json()
    member_library.save_member_to_json()
    if returning and member_returning:
        print("Book returned sucessfully")
    elif returning is None:
        print("Book not found")
    elif member_returning is None:
        print("Member not found")
    else:
        print("Return failed. All copies are already available.")


def search_book_menu(library):
    book_id=total_copies_validation("Enter book ID: ")
    searching=library.find_book_by_id(book_id)
    if searching is None:
        print("Book not found")
    else:
        print(searching)

def display_allbook_menu(library):
    books=library.get_all_books()
    if books:
        for book in books:
            print(book)
    else:
        print("No books added")
