from library import Library
from menu import *
from member_menu import *
from member_library import Member_library

print("========== Library Management System ==========")

library=Library()
library.load_from_json()
member_library=Member_library()
member_library.load_member_from_json()

while True:
    
    menu(library)
    choice=input("Enter your choice: ")

    if choice=="1":
        add_book_menu(library)
    elif choice=="2":
        borrow_book_menu(library, member_library)
    elif choice=="3":
        return_book_menu(library, member_library)
    elif choice=="4":
        search_book_menu(library)
    elif choice=="5":
        display_allbook_menu(library)
    elif choice=="6":
        add_member(member_library)
    elif choice=="7":
        search_member(member_library)
    elif choice=="8":
        display_all_members(member_library)
    elif choice=="0":
        print("Thank you for using the Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")