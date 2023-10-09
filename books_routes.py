from flask import Flask, request, Blueprint
from book import Book
from marshmallow_error import BookValidation

book_blueprint = Blueprint("Book Module", __name__, url_prefix="/books")


@book_blueprint.route('/')
def welcome_page():
    return "Welcome to Book Store"


@book_blueprint.route('/getallbooks/')
def get_all_books():
    sorted_query = request.args.get('sorted_by', default='id')    # Receive args from postman
    filter_query = request.args.get('filter_by')                  # Receive args from postman
    data = Book.get_all(sorted_query, filter_query)                # Passing args to that function
    return data


@book_blueprint.route('/checkbook/')
def check_book():
    check_query_auth = request.args.get('check_query_author')  # Receive args from postman
    check_query_tit = request.args.get('check_query_title', default='java')
    result = Book.check_book(check_query_auth, check_query_tit)
    return result


@book_blueprint.route('/create/', methods=['POST'])
def create_book():
    input_dict = request.json  # Receives data from postman
    book = BookValidation().load(input_dict)    # Load that Json dictionary to the marshmallo class

    call = Book(title=input_dict['title'], author_name=input_dict['author_name'], serial=input_dict['serial']).create_a_book()
    return call


@book_blueprint.route('/update/', methods=['PUT'])
def update_book():
    call = Book.update()
    return call


@book_blueprint.route('/delete/', methods=['DELETE'])
def delete_books():
    call = Book.delete_all()
    return call


@book_blueprint.route('/boookupdate/', methods=['PUT'])
def update():
    book = Book(title='new java', author_name='newraj', serial='55')
    call = book.update_dict()
    return call


@book_blueprint.route('/updatebook/byid/<id>/', methods=['PUT'])
def update_id(id: int):
    book = Book.update_by_id(id)
    return book


@book_blueprint.route('/deletebook/byid/', methods=['DELETE'])
def delete_a_book():
    book_id = request.args.get('delete_by_id')
    book = Book.delete_a_book(book_id)
    return book


@book_blueprint.route('/getbook/byid/<id>/')   # Example of route Parameters
def get_by_id(id: int):
    book = Book.get_book_by_id(id)
    return book


