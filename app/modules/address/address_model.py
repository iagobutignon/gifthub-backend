class AddressModel:
    def __init__(self, data):
        self.cep = data['cep']
        self.number = ''
        self.street = data['logradouro']
        self.district = data['bairro']
        self.city = data['localidade']
        self.state = data['uf']

    def toJson(self):
        return {
            'number': self.number,
            'cep': self.cep,
            'street': self.street,
            'district': self.district,
            'city': self.city,
            'state': self.state
        }