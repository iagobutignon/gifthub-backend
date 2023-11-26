from flask import Blueprint, request


auth_blueprint = Blueprint("auth", __name__)


class AuthController():
    @auth_blueprint.post("/sign_up")
    def sign_up():
        data = request.get_json()

        name = data['name']
        surname = data['surname']
        email = data['email']
        password = data['password']

        return {
            'email': email,
            'password': password,
            'name': name,
            'surname': surname,
        }, 201

    @auth_blueprint.post("/sign_in")
    def sign_in():
        data = request.get_json()

        email = data['email']
        password = data['password']

        return {
            'email': email,
            'password': password,
        }, 200

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
