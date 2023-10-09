import json

class Person:
    def __init__(self, name: str):
        self.name = name
        self.id = 1

    @staticmethod
    def open_file(data):  # Function is called everytime so we made separate function
        with open('persondata.json', "w") as file:
            new_data_json = json.dumps(data)  # Encoding
            file.write(new_data_json)

    @staticmethod
    def get_all_customers(sort_by='id'):
        try:
            file = open('persondata.json')
            data = json.load(file)
            data = sorted(data, key=lambda item: item[sort_by])
            return data
        except json.decoder.JSONDecodeError:  # if file is there but there is no data
            return []

    def create_user(self):
        data = Person.get_all_customers()
        if data:
            last_item = data[-1]['id']
            last_item = last_item + 1
            self.id = last_item
        new_dict = {'id': self.id, 'name': self.name}
        data.append(new_dict)
        Person.open_file(data)
        return "User Created"

    @staticmethod
    def update_user(id, parameter):  # receives args from routes file
        data = Person.get_all_customers()
        try:
            target = [item for item in data if item['id'] == int(id)]  # checks the id
            if int(id) > data[-1]['id']:
                raise IndexError
        except IndexError as e:
                return f"Please Enter valid id you have entered,The id of last Person is : {data[-1]['id']}"

        target[0]['name'] = parameter
        call = Person.open_file(data)
        return "The data got updated"

    @classmethod
    def delete_all(cls, id=None):
        data = cls.get_all_customers()
        if id:                               # delete if id was given
            for item in data:
                if item['id'] == int(id):
                    data.remove(item)
                    cls.open_file(data)
                    return data
        with open('persondata.json', 'w') as file:  # delete all books if id was not given
            json.dumps(data)
            file.write('[]')
            call = cls.get_all_customers()
            return call
