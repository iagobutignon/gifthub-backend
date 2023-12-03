from app.modules.shared.errors import Errors
from app.modules.infra.database import users
from app.modules.user.user_model import UserModel
from app.modules.infra.database import database


class UserRepository:
    def getUsers():
        users = UserModel.query.all()

        return users

    def getUserById(id):
        user = UserModel.query.filter_by(id=id).first()

        print(user)
        
        if user == None:
            raise Errors.userNotFound()
        
        return user

    def getUserByCredential(email, password):
        user = UserModel.query.filter_by(email=email).first()
        
        if user == None:
            raise Errors.userNotFound()
        if user.password != password:
            raise Errors.invalidPassword()
        
        return user

    def createUser(userModel):
        try:
            database.session.add(userModel)
            database.session.commit()

            return userModel
        except:
            raise Errors.userAlreadyExists()
    
    def updateUser(id, userModel):
        user = UserModel.query.filter_by(id=id).first()

        if user == None:
            raise Errors.userNotFound()

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
        
    def updateUserPicture(id, userPicture):
        user = UserModel.query.filter_by(id=id).first()

        if user == None:
            raise Errors.userNotFound()

        user.picture = userPicture

        database.session.commit()

        return user

    def deleteUser(id):
        user = UserModel.query.filter_by(id=id).first()
        
        if user == None:
            raise Errors.userNotFound()
        
        database.session.delete(user)
        database.session.commit()

        return user
    
    def updatePassword(email, password, newPassword):
        user = UserModel.query.filter_by(email=email).first()

        if user == None:
            raise Errors.userNotFound()
        if user.password != password:
            raise Errors.invalidPassword()
        
        user.password = newPassword

        database.session.commit()

        return user
