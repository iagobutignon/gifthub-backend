from app.modules.shared.custom_error import CustomError


class Errors :
    #User erros
    def userNotFound(): return CustomError(100, "Usuário não encontrado", 404)
    def userAlreadyExists(): return CustomError(101, "Email já cadastrado", 403)
    def invalidPassword(): return CustomError(102, "Senha incorreta", 403)

    #Event errors
    def eventNotFound(): return CustomError(200, "Evento não encontrado", 404)
    
    #Product errors
    def productNotFound(): return CustomError(300, "Produto não encontrado", 404)