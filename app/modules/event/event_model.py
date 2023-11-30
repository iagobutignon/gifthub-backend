from app.modules.shared.address_model import AddressModel
from app.modules.shared.guid import Guid


class EventModel:
    def __init__(self, data):
        self.id = Guid.new()
        self.name = data['name']
        self.date = data['date']
        self.description = data['description']
        self.address = AddressModel(data['address'])

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'description': self.description,
            'address': odeioPython(self.address),
        }
    
def odeioPython(address):
    if address != None:
        return address.toJson()
    else:
        return None