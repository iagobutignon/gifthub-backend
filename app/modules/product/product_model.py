from app.modules.shared.guid import Guid


class ProductModel:
    def __init__(self, data):
        self.id = Guid.new()
        self.name = data['name']

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
        }