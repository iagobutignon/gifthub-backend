import json
import uuid

class UserModel:
    def __init__(self, data):
        self.id = uuid.uuid4()
        self.name = data['name']
        self.surname = data['surname']
        self.email = data['email']
        self.password = data['password']