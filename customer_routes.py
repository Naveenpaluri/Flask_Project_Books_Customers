from flask import request, Blueprint
from customer import Person
from marshmallow_error import CustomerValidation

customer_blueprint = Blueprint("Customer Module", __name__, url_prefix="/customer")


@customer_blueprint.route('/')
def home():
    return "This is Home Page"


@customer_blueprint.route('/create/', methods=['POST'])
def create_customer():
    request_parameters = request.args.get('Name')    # gets query parameters from Postman
    valid_dict = {'name': request_parameters}     # create a dummy dictionary for using marshmello
    person_validation = CustomerValidation().load(valid_dict)   # load that dict into marshmello module
    person = Person(**valid_dict).create_user()           # unpacking of dictionary
    return "User Created"


@customer_blueprint.route('/list/')
def get_all():
    sort_query = request.args.get('sort_by', default='name')
    call = Person.get_all_customers(sort_query)
    return call


@customer_blueprint.route('/update/<id>', methods=['PUT'])
def update_customer(id: int):
    query_parameters = request.args.get('Name')
    call = Person.update_user(id=id, parameter=query_parameters)
    return call


@customer_blueprint.route('/delete/', methods=['DELETE'])
def delete_customer():
    delete_id_query = request.args.get('id')
    call = Person.delete_all(id=delete_id_query)
    return call

