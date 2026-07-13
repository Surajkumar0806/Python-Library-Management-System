from book import Book
from storage import *



class Library:
    def __init__(self):
        self.books=[]

    def add_book(self, book):
        excisting_book=self.find_book_by_id(book.book_id)
        if excisting_book is None:
            self.books.append(book)
            return True
        else:
            excisting_book.total_copies+=1
            excisting_book.available_copies+=1
            return False
    
    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id==book_id:
                return book
        return None
        
    def borrow_book(self, book_id):
        book_for_borrow=self.find_book_by_id(book_id)
        if book_for_borrow is None:
            return None
        return book_for_borrow.borrow()
    
    def get_all_books(self):
        return tuple(self.books)

    def return_book(self, book_id):
        book_for_return= self.find_book_by_id(book_id)
        if book_for_return is None:
            return None
        return book_for_return.return_copy()
    
    def save_to_json(self):
        book_data=[]
        for book in self.books:
            book_data.append(book.to_dict())

        with open(json_path, "w") as file:
            json.dump(book_data, file, indent=4)


    def load_from_json(self):
        data=load_books_data()
        for book_data in data:
            book= Book.from_dict(book_data)
            self.books.append(book)
