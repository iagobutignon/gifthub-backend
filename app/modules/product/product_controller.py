from flask import Blueprint, request


product_blueprint = Blueprint("product", __name__)


class ProductController():
    @product_blueprint.get("/<id>")
    def get_product(id):
        try:
            None
            # TODO: Implementar get_product
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }  

    @product_blueprint.get("/")
    def get_products():
        try:
            None
            # TODO: Implementar get_products
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }  

    @product_blueprint.post("/")
    def create_product():
        try:
            None
            # TODO: Implementar create_product
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }  

    @product_blueprint.put("/<id>")
    def edit_product(id):
        try:
            None
            # TODO: Implementar edit_product
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }  

    @product_blueprint.delete("/<id>")
    def delete_product():
        try:
            None
            # TODO: Implementar delete_product
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }  
