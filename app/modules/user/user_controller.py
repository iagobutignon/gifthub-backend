from app.modules.shared.custom_error import CustomError
from app.modules.user.user_repository import UserRepository
from flask import Blueprint, request

from app.modules.user.user_model import UserModel


user_blueprint = Blueprint("user", __name__)


class UserController():
    @user_blueprint.get("/")
    def get():
        try:
            result = UserRepository.get_users()

            return [e.toJson() for e in result]
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @user_blueprint.get("/<id>")
    def get_user(id):
        try:
            result = UserRepository.get_user_by_id(id)
            
            return result.toJson(), 200
        
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @user_blueprint.post("/")
    def sign_up():
        try:
            data = request.get_json(force=True,silent=True)
            user = UserModel(data)
            result = UserRepository.create_user(user)

            return result.toJson(), 201
        
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @user_blueprint.put("/<id>")
    def edit_user(id):
        try:
            data = request.get_json()
            user = UserModel(data)
            result = UserRepository.update_user(id, user)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
    
    @user_blueprint.delete("/<id>")
    def delete_user(id):
        try:
            result = UserRepository.delete_user(id)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
        
    @user_blueprint.post("/sign_in")
    def sign_in():
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            result = UserRepository.get_user_by_credential(email, password)

            return result.toJson(), 200
        
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @user_blueprint.put("/update_picture/<id>")
    def update_picture(id):
        try:
            picture = request.json['picture']
            result = UserRepository.update_user_picture(id, picture)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @user_blueprint.post("/forgot_password")
    def forgot_password():
        try:
            None
            # TODO: Implementar forgot_password
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @user_blueprint.post("/update_password")
    def update_password():
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            new_password = data['new_password']

            result = UserRepository.update_password(email, password, new_password)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
