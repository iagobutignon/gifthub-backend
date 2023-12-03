from flask import Blueprint

from app.modules.address.address_service import AddressService
from app.modules.shared.custom_error import CustomError

address_blueprint = Blueprint("address", __name__)

class AddressController:
    @address_blueprint.get("/get_address_by_cep/<cep>")
    def get_address_by_cep(cep):
        try:
            result = AddressService.get_address_by_cep(cep)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()