from flask import Blueprint, request

from app.modules.address.address_service import AddressService

address_blueprint = Blueprint("address", __name__)

class AddressController:
    @address_blueprint.get("/get_address_by_cep/<cep>")
    def get_address_by_cep(cep):
        try:
            result = AddressService.getAddressByCep(cep)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]