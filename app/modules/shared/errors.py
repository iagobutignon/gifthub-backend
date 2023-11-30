class Errors :
    #User erros
    def userNotFound(): return Exception(100, "Usuário não encontrado", 404)
    def userAlreadyExists(): return Exception(101, "Email já cadastrado", 403)
    def invalidPassword(): return Exception(102, "Senha incorreta", 403)

    #Event errors
    def eventNotFound(): return Exception(200, "Evento não encontrado", 404)
    
    #Product errors
    def productNotFound(): return Exception(300, "Produto não encontrado", 404)