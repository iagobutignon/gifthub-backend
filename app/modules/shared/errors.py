class Errors:
    #User erros
    def userNotFound(): Exception(100, "Usuário não encontrado", 404)
    def userAlreadyExists(): Exception(101, "Email já cadastrado", 403)
    def invalidPassword(): Exception(102, "Senha incorreta", 403)

    #Event errors
    def eventNotFound(): Exception(200, "Evento não encontrado", 404)
    
    #Product errors
    def productNotFound(): Exception(200, "Produto não encontrado", 404)