from validation import *
from member import Member
from member_library import Member_library

def add_member(member_library):
    member_id=total_copies_validation("Enter the member ID: ")
    name=text_validation("Enter the member name: ")
    phone=total_copies_validation("Enter the phone number")
    email=input("Enter the email of the member")
    member=Member(member_id, name, phone, email)
    added=member_library.add_member(member)
    member_library.save_member_to_json()
    if added:
        print("Member added successfully ")
    else:
        print("Member already exist")
def search_member(member_library):
    membersid_searching=total_copies_validation("Enter the member Id")
    searching=member_library.find_member_by_id(membersid_searching)
    if searching is None:
        print("Member not found")
    else:
        print(searching)
def display_all_members(member_library):
    members=member_library.get_all_members()
    if members:
        for member in members:
            print(member)
    else:
        print("No member entered")
