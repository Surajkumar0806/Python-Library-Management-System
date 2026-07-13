from member import Member
from storage import *

class Member_library:
    def __init__(self):
        self.members=[]

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id==member_id:
                return member
        return None

    def add_member(self, member):
        exsisting_member=self.find_member_by_id(member.member_id)
        if exsisting_member is None:
            self.members.append(member)
            return True
        else:
            return False
        
    def get_all_members(self):
        return tuple(self.members)
            
    def borrow_book_member(self, member_id, book_id):
        member_for_borrow=self.find_member_by_id(member_id)
        if member_for_borrow is None:
            return None
        return member_for_borrow.borrow(book_id)

    def return_book(self, member_id, book_id):
        book_for_return= self.find_member_by_id(member_id)
        if book_for_return is None:
            return None
        return book_for_return.return_book_member(book_id)
    
    def save_member_to_json(self):
        member_data=[]
        for member in self.members:
            member_data.append(member.to_dict())

        with open(json_member_path, "w") as file:
            json.dump(member_data, file, indent=4)

    def load_member_from_json(self):
        data=load_members_data()
        for member_data in data:
            member= Member.from_dict(member_data)
            self.members.append(member)