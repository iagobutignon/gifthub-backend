from app.modules.shared.errors import Errors
from app.modules.user.user_model import UserModel
from app.modules.infra.database import database


class UserRepository:
    def get_users():
        users = UserModel.query.all()

        return users

    def get_user_by_id(id):
        user = UserModel.query.filter_by(id=id).first()
        
        if user == None:
            raise Errors.user_not_found()
        
        return user

    def get_user_by_credential(email, password):
        user = UserModel.query.filter_by(email=email).first()
        
        if user == None:
            raise Errors.user_not_found()
        if user.password != password:
            raise Errors.invalid_password()
        
        return user

    def create_user(user_model):
        try:
            database.session.add(user_model)
            database.session.commit()

            return user_model
        except:
            raise Errors.user_already_exists()
    
    def update_user(id, user_model):
        user = UserModel.query.filter_by(id=id).first()

        if user == None:
            raise Errors.user_not_found()

        user.email = user_model.email or user.email
        user.password = user_model.password or user.password
        user.name = user_model.name or user.name
        user.surname = user_model.surname or user.surname
        user.description = user_model.description or user.description
        user.cep = user_model.cep or user.cep
        user.number = user_model.number or user.number
        user.street = user_model.street or user.street
        user.district = user_model.district or user.district
        user.city = user_model.city or user.city
        user.state = user_model.state or user.state
        user.complement = user_model.complement or user.complement

        database.session.commit()

        return user
        
    def update_user_picture(id, user_picture):
        user = UserModel.query.filter_by(id=id).first()

        if user == None:
            raise Errors.user_not_found()

        user.picture = user_picture

        database.session.commit()

        return user

    def delete_user(id):
        user = UserModel.query.filter_by(id=id).first()
        
        if user == None:
            raise Errors.user_not_found()
        
        database.session.delete(user)
        database.session.commit()

        return user
    
    def update_password(email, password, new_password):
        user = UserModel.query.filter_by(email=email).first()

        if user == None:
            raise Errors.user_not_found()
        if user.password != password:
            raise Errors.invalid_password()
        
        user.password = new_password

        database.session.commit()

        return user
