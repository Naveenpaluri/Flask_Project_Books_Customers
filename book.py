import json

class Book:
    def __init__(self, title: str, author_name: str, serial: str):
        self.title = title
        self.author_name = author_name
        self.serial = serial
        self.id = 1

    @staticmethod
    def get_all(sorted_by='id', filter_by=None):  # Fetches all the books present in the store
        try:
            file = open('bookdata.json')
            data = json.load(file)
            if filter_by:
                data = filter(lambda item: filter_by in item['author_name'], data)
            data = sorted(data, key=lambda item: item[sorted_by])

            return data
        except json.decoder.JSONDecodeError:  # if file is there but there is no data
            return []
        except KeyError:                        # if key is not there {}
            return "There is no key exists !!!"
        except FileNotFoundError:                # If file not found
            return []

    def check_duplicate_serial(self, books):

        # Function that checks if any duplicate serial numbers exists or not
        for item in books:
            if item['serial'] == self.serial:
                raise Exception("The Serial number already Exists")

    @staticmethod
    def open_file(books):    # Function is called everytime so we made separate function
        with open('bookdata.json', "w") as file:
            new_data_json = json.dumps(books)  # Encoding
            file.write(new_data_json)


    @staticmethod
    def check_book(check_query_author=None, check_query_title=None):  # This function takes input from postman
        books = Book.get_all()
        if check_query_author:
            result = [item for item in books if item['author_name'] == check_query_author]
        else:
            result = list(filter(lambda item: item['title'] == check_query_title, books))

        return result

    def create_a_book(self):
        books = self.__class__.get_all()
        if books:
            last_item = books[-1]['id']
            self.id = last_item + 1
        new_dict = {'id': self.id, 'title': self.title, 'author_name': self.author_name, 'serial': self.serial}
        # self.__class__.check_duplicate_serial(self, books)
        # Checks the duplicate keys in the books list
        books.append(new_dict)
        Book.open_file(books)
        return "Book Created"


    @staticmethod
    def update():
        books = Book.get_all()
        for item in books:
            item['title'] = item['title'] + "12.2"
            item['author_name'] = item['author_name']+'Kumar'

        Book.open_file(books)
        Book.get_all()
        return "Book Updated"

    @staticmethod
    def delete_all():
        books = Book.get_all()
        with open('bookdata.json', 'w') as file:
            json.dumps(books)
            file.write('[]')
        call = Book.get_all()
        return call

    def update_dict(self):
        books = self.__class__.get_all()
        target_name = 'raj'
        target_title = 'java'
        for items in books:
            if items['author_name'] == target_name and items['title'] == target_title:
                items['author_name'] = self.author_name
                items['title'] = self.title
                items['serial'] = self.serial
        Book.open_file(books)
        call = self.__class__.get_all()
        return call

    @staticmethod
    def update_by_id(id: int):

        books = Book.get_all()
        filter_book = [item for item in books if int(item['id']) == int(id)]
        filter_book = filter_book[0]
        filter_book['title'] = "This is New Titled Book"
        filter_book['author_name'] = "New updated author"
        Book.open_file(books)
        return filter_book

    @staticmethod
    def delete_a_book(delete_by_id=None):
        delete_by_id = int(delete_by_id)
        books = Book.get_all()
        filter_item = list(filter(lambda item: int(item['id']) == delete_by_id, books))
        books.remove(filter_item[0])
        Book.open_file(books)
        return "Book Got Deleted"

    @classmethod
    def get_book_by_id(cls, id: int):
        books = cls.get_all()
        id = int(id)
        target_book = list(filter(lambda item: item['id'] == id, books))
        return target_book











