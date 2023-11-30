from app.modules.shared.address_model import AddressModel
from app.modules.shared.guid import Guid


class UserModel:
    def __init__(self, data):
        self.id = Guid.new()
        try: 
            self.name = data['name']
        except:
            self.name = None
        try:
            self.surname = data['surname']
        except:
            self.surname = None
        try:
            self.email = data['email']
        except:
            self.email = None
        try:
            self.password = data['password']
        except:
            self.password = None
        try:
            self.description = data['description']
        except:
            self.description = None
        try:
            self.address = AddressModel(data['address'])
        except:
            self.address = None

        
    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'description': self.description,
            'address': odeioPython(self.address),
        }

def odeioPython(address):
    if address != None:
        return address.toJson()
    else:
        return None