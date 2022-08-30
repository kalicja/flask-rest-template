import json

from flask_rest_demo.commons.common_eq import CommonEqualityMixin


class Hello(CommonEqualityMixin):
    def __init__(self, greeting, sender):
        self.greeting = greeting
        self.sender = sender


class HelloEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class HelloRepo:
    def __init__(self):
        self.hellos = {}
        self.last_id = 0

    def get_all(self):
        return list(self.hellos.values())

    def get(self, id):
        if id not in self.hellos.keys():
            return None
        return self.hellos[id]

    def save(self, hello):
        self.last_id+=1
        self.hellos[id]=hello

    def delete(self, id):
        self.hellos.pop(id)

