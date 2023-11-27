users = []

class UserRepository:
    def getUserByCredential(email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user

    def insertUser(userModel):
        for user in users:
            if user.email == userModel.email:
                raise Exception('Usuario ja cadastrado')

        users.append(userModel)
            
        return userModel