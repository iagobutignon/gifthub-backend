from app.modules.shared.address_model import AddressModel
from app.modules.shared.guid import Guid


class EventModel:
    def __init__(self, data):
        self.id = Guid.new()
        try: 
            self.userId = data['user_id']
        except:
            self.userId = None
        try: 
            self.name = data['name']
        except:
            self.name = None
        try: 
            self.description = data['description']
        except:
            self.description = None
        try: 
            self.date = data['date']
        except:
            self.date = None
        try: 
            self.time = data['time']
        except:
            self.time = None
        try: 
            self.image = data['image']
        except:
            self.image = None
        try: 
            self.address = AddressModel(data['address'])
        except:
            self.address = None

    def toJson(self):
        return {
            'id': self.id,
            'user_id': self.userId,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'time': self.time,
            'image': self.image,
            'address': odeioPython(self.address),
        }
    
def odeioPython(address):
    if address != None:
        return address.toJson()
    else:
        return None