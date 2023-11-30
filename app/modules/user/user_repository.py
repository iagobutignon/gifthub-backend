from app.modules.shared.errors import Errors
from app.modules.infra.database import users


class UserRepository:
    def getUserById(id):
        for user in users:
            if user.id == id:
                return user
            
        raise Errors.userNotFound()

    def getUserByCredential(email, password):
        for user in users:
            if user.email == email:
                if user.password == password:
                    return user
                else:
                    raise Errors.invalidPassword()
        
        raise Errors.userNotFound()

    def createUser(userModel):
        for user in users:
            if user.email == userModel.email:
                raise Errors.userAlreadyExists()

        users.append(userModel)
            
        return userModel
    
    def updateUser(id, userModel):
        user = None
        for u in users:
            if u.id == id:
                user = u
                break
        
        if user == None:
            raise Errors.userNotFound()
        
        user.name = userModel.name or user.name
        user.surname = userModel.surname or user.surname
        user.email = userModel.email or user.email
        user.description = userModel.description or user.description
        user.address = userModel.address or user.address

        return user
    
    def updateUserPicture(id, userPicture):
        user = None
        for u in users:
            if u.id == id:
                user = u
                break
        
        if user == None:
            raise Errors.userNotFound()
        
        user.picture = userPicture

        return user

    def deleteUser(id):
        user = None
        for u in users:
            if u.id == id:
                user = u
                break
        
        if user == None:
            raise Errors.userNotFound()
        
        users.remove(user)

        return user
    
    def updatePassword(email, password, newPassword):
        for user in users:
            if user.email == email:
                if user.password == password:
                    user.password = newPassword
                    return user
                else:
                    raise Errors.invalidPassword()
        
        raise Errors.userNotFound()
