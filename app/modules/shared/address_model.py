from app.modules.shared.guid import Guid


class AddressModel:
    def __init__(self, data):
        self.id = Guid.new()
        try:
            self.number = data['number']
        except:
            self.number = None
        try:
            self.street = data['street']
        except:
            self.street = None
        try:
            self.district = data['district']
        except:
            self.district = None
        try:
            self.city = data['city']
        except:
            self.city = None
        try:
            self.state = data['state']
        except:
            self.state = None
        try:
            self.cep = data['cep']
        except:
            self.cep = None
        try:
            self.complement = data['complement']
        except:
            self.complement = None

    def toJson(self):
        return {
            'id': self.id,
            'number': self.number,
            'street': self.street,
            'district': self.district,
            'city': self.city,
            'state': self.state,
            'cep': self.cep,
            'complement': self.complement
        }