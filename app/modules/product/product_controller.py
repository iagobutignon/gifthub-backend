from flask import Blueprint, request
from app.modules.product.product_model import ProductModel

from app.modules.product.product_repository import ProductRepository


product_blueprint = Blueprint("product", __name__)


class ProductController():
    @product_blueprint.get("/")
    def get_products():
        try:
            result = ProductRepository.getProducts()

            return [e.toJson() for e in result], 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
        
    @product_blueprint.get("/get_products_by_event_id/<id>")
    def get_products_by_event_id(id):
        try:
            result = ProductRepository.getProductsByEventId(id)
            
            return [e.toJson() for e in result], 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
        

    @product_blueprint.get("/<id>")
    def get_product(id):
        try:
            result = ProductRepository.getProductById(id)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
        
    @product_blueprint.post("/")
    def create_product():
        try:
            data = request.get_json(force=True,silent=True)
            product = ProductModel(data)
            result = ProductRepository.createProduct(product)

            return result.toJson(), 201
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]

    @product_blueprint.put("/<id>")
    def edit_product(id):
        try:
            data = request.get_json()
            product = ProductModel(data)
            result = ProductRepository.updateProduct(id, product)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]

    @product_blueprint.delete("/<id>")
    def delete_product(id):
        try:
            result = ProductRepository.deleteProduct(id)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
