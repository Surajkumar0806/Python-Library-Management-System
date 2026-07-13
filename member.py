

class Member():
    def __init__(self, member_id, name, phone, email, borrowed_books=None):
        self.member_id=member_id
        self.name=name
        self.phone=phone
        self.email=email
        if borrowed_books is None:
            self.borrowed_books=[]
        else:
            self.borrowed_books=borrowed_books

    def borrow(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False
    
    def return_book_member(self, returning):
        for book_id in self.borrowed_books:
            if book_id==returning:
                self.borrowed_books.pop(self.borrowed_books.index(returning))
                return True
        return None
    
    def get_borrowed_count(self):
        return len(self.borrowed_books)
    
    def __str__(self):
        return (
            f" Member ID: {self.member_id}\n"
            f" Name: {self.name}\n"
            f" Phone.No: {self.phone}\n"
            f" Email: {self.email}\n"
        )

    def borrowed_book_to_dict(self):
        borrowed_books_data = []
        for book in self.borrowed_books:
            borrowed_books_data.append(book.to_dict())
        return borrowed_books_data

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["member_id"],
            data["name"],
            data["phone"],
            data["email"],
            data["borrowed_books"]
        )
