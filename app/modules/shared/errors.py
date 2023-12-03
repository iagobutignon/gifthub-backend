from app.modules.shared.custom_error import CustomError


class Errors :
    #User erros
    def user_not_found(): return CustomError(100, "Usuário não encontrado", 404)
    def user_already_exists(): return CustomError(101, "Email já cadastrado", 403)
    def invalid_password(): return CustomError(102, "Senha incorreta", 403)

    #Event errors
    def event_not_found(): return CustomError(200, "Evento não encontrado", 404)
    
    #Product errors
    def product_not_found(): return CustomError(300, "Produto não encontrado", 404)