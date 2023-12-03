import requests

from app.modules.address.address_model import AddressModel

class AddressService:
    def getAddressByCep(cep):

        result = requests.get('https://viacep.com.br/ws/' + cep + '/json/')
        print(result.json())
        address = AddressModel(result.json())
        return address