from app.modules.shared.guid import Guid


class ProductModel:
    def __init__(self, data):
        self.id = Guid.new()
        try: 
            self.eventId = data['event_id']
        except:
            self.eventId = None
        try:
            self.image = data['image']
        except:
            self.image = None
        try:
            self.name = data['name']
        except:
            self.name = None
        try:
            self.value = data['value']
        except:
            self.value = None
        try:
            self.description = data['description']
        except:
            self.description = None

    def toJson(self):
        return {
            'id': self.id,
            'event_id': self.eventId,
            'image': self.image,
            'name': self.name,
            'value': self.value,
            'description': self.description,
        }