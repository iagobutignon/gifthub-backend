from app.modules.shared.errors import Errors
from app.modules.user.user_model import UserModel
from app.modules.infra.database import database


class UserRepository:
    def get_users():
        users = UserModel.query.all()

        return users

    def get_user_by_id(id):
        user = UserModel.query.filter_by(id=id).first()

        print(user)
        
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

    def create_user(userModel):
        try:
            database.session.add(userModel)
            database.session.commit()

            return userModel
        except:
            raise Errors.user_already_exists()
    
    def update_user(id, userModel):
        user = UserModel.query.filter_by(id=id).first()

        if user == None:
            raise Errors.user_not_found()

        user.email = userModel.email or user.email
        user.password = userModel.password or user.password
        user.name = userModel.name or user.name
        user.surname = userModel.surname or user.surname
        user.description = userModel.description or user.description
        user.cep = userModel.cep or user.cep
        user.number = userModel.number or user.number
        user.street = userModel.street or user.street
        user.district = userModel.district or user.district
        user.city = userModel.city or user.city
        user.state = userModel.state or user.state
        user.complement = userModel.complement or user.complement

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
