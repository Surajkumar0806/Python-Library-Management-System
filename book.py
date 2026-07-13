class Book:
    def __init__(self, book_id, title, author, section, total_copies, available_copies=None):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.section=section
        self.total_copies=total_copies
        if available_copies is None:
            self.available_copies=total_copies
        else:
            self.available_copies=available_copies

    
    def __str__(self):
        return (
                    f"book_id: {self.book_id}\n"
                    f"Title: {self.title}\n"
                    f"Author: {self.author}\n"
                    f"Section: {self.section}\n"
                    f"Total Copies: {self.total_copies}\n"
                    f"Available Copies: {self.available_copies}"
                )

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "section":self.section,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies
        }

    

    def borrow(self):
        if self.available_copies>0:
            self.available_copies-=1
            return True
        return False
    
    def return_copy(self):
        if self.available_copies<self.total_copies:
            self.available_copies+=1
            return True
        return False
    @classmethod
    def from_dict(cls, data):
        return  cls(
                            data["book_id"],
                            data["title"],
                            data["author"],
                            data["section"],
                            data["total_copies"],
                            data["available_copies"]
                        )
    