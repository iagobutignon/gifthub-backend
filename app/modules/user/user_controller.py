from app.modules.user.user_repository import UserRepository
from flask import Blueprint, request

from app.modules.user.user_model import UserModel


user_blueprint = Blueprint("user", __name__)


class UserController():
    @user_blueprint.get("/<id>")
    def get_user(id):
        try:
            result = UserRepository.getUserById(id)
            
            return result.toJson(), 200
        
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]

    @user_blueprint.post("/")
    def sign_up():
        try:
            data = request.get_json(force=True,silent=True)
            user = UserModel(data)
            result = UserRepository.createUser(user)

            return result.toJson(), 201
        
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]

    @user_blueprint.put("/<id>")
    def edit_user(id):
        try:
            data = request.get_json()
            user = UserModel(data)
            result = UserRepository.updateUser(id, user)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
    
    @user_blueprint.delete("/<id>")
    def delete_user(id):
        try:
            result = UserRepository.deleteUser(id)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
        
    @user_blueprint.post("/sign_in")
    def sign_in():
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            result = UserRepository.getUserByCredential(email, password)

            return result.toJson(), 200
        
        except Exception as e:
            print(e)
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]

    @user_blueprint.put("/update_picture/<id>")
    def update_picture(id):
        try:
            picture = request.json['picture']
            result = UserRepository.updateUserPicture(id, picture)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }

    @user_blueprint.post("/forgot_password")
    def forgot_password():
        try:
            None
            # TODO: Implementar forgot_password
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }

    @user_blueprint.post("/update_password")
    def update_password():
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            newPassword = data['newPassword']

            result = UserRepository.updatePassword(email, password, newPassword)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }
