from app.modules.auth.user_repository import UserRepository
from flask import Blueprint, request

from app.modules.auth.user_model import UserModel


auth_blueprint = Blueprint("auth", __name__)


class AuthController():
    @auth_blueprint.post("/sign_up")
    def sign_up():
        try:
            data = request.get_json()
            user = UserModel(data)
            saveduser = UserRepository.insertUser(user)

            return {
                'id': saveduser.id,
                'email': saveduser.email,
                'password': saveduser.password,
                'name': saveduser.name,
                'surname': saveduser.surname,
            }, 201
        except:
            return {
                'mensagem': 'Usuario já cadastrado'
            }, 403

    @auth_blueprint.post("/sign_in")
    def sign_in():
        try:
            data = request.get_json()

            email = data['email']
            password = data['password']

            user = UserRepository.getUserByCredential(email, password)
            print(user)
            return {
                'email': user.email,
                'password': user.password,
            }, 200
        except:
            return {
                'mensagem': 'Ocorreu um erro ao fazer  o login'
            }, 403

    # @auth_blueprint.post("/edit_user")
    # def edit_user():
    #     data = request.get_json()

    #     return data, 200

    # @auth_blueprint.post("/forgot_password")
    # def forgot_password():
    #     data = request.get_json()

    #     return data, 200

    # @auth_blueprint.post("/change_password")
    # def change_password():
    #     data = request.get_json()

    #     return data, 200
