import unittest
from book import Book


class TestBookStore(unittest.TestCase):

    def test_get_all(self):
        func_call_data = Book.get_all()
        assert isinstance(func_call_data, list)  # Check if instance of list

    def test_create_book(self):
        data_dict = {'title': 'Jaguar', 'author_name': 'Napolean', 'serial': '668'}
        books = Book.get_all()
        book_instance = Book(**data_dict)                 # create an object instance
        book_instance.check_duplicate_serial(books)       # call function using object
        func_call = book_instance.create_a_book()         # call function using object
        assert func_call == "Book Created"

    def test_check_book(self):
        func_call = Book.check_book()
        assert isinstance(func_call, list)  # Check if instance of list
    """   
    def test_delete_all(self):
        func_call = Book.check_book()
        assert isinstance(func_call, list)  # Check if instance of list
    
    
    def test_delete_by_id(self):
        func_call = Book.delete_a_book(delete_by_id=12)
        assert func_call == "Book Got Deleted"
        
    """
    def test_getbook_by_id(self):
        func_call = Book.get_book_by_id(13)
        assert isinstance(func_call, list)








