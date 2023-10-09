import unittest
from customer import Person


class TestCustomerInfo(unittest.TestCase):

    def test_get_all(self):
        func_call = Person.get_all_customers()   # Call the function in Person class
        assert isinstance(func_call, list)

    def test_create_user(self):
        test_obj = {'name': 'Rajan'}
        func_call = Person(**test_obj).create_user()

        # create an object for Person class and call the function create user()

        assert func_call == "User Created"

    def test_update_by_id(self):
        func_call = Person.update_user(id=4, parameter='KING')   # Call the function in Person class
        assert func_call == "The data got updated"

    """
    def test_delete(self):
        func_call = Person.delete_all()
        assert isinstance(func_call, list)
    """
