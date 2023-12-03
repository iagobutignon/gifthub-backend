import json
from flask import Blueprint, request, send_file
from app.modules.product.product_model import ProductModel

from app.modules.product.product_repository import ProductRepository
from app.modules.product.product_service import ProductService
from app.modules.shared.custom_error import CustomError


product_blueprint = Blueprint("product", __name__)


class ProductController():
    @product_blueprint.get("/")
    def get_products():
        try:
            result = ProductRepository.get_products()

            return [e.toJson() for e in result], 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
        
    @product_blueprint.get("/get_products_by_event_id/<id>")
    def get_products_by_event_id(id):
        try:
            result = ProductRepository.get_products_by_event_id(id)
            
            return [e.toJson() for e in result], 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
        

    @product_blueprint.get("/<id>")
    def get_product(id):
        try:
            result = ProductRepository.get_product_by_id(id)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
        
    @product_blueprint.post("/")
    def create_product():
        try:
            data = request.get_json(force=True,silent=True)
            product = ProductModel(data)
            result = ProductRepository.create_product(product)

            return result.toJson(), 201
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @product_blueprint.put("/<id>")
    def update_product(id):
        try:
            data = request.get_json()
            product = ProductModel(data)
            result = ProductRepository.update_product(id, product)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @product_blueprint.delete("/<id>")
    def delete_product(id):
        try:
            result = ProductRepository.delete_product(id)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403

    @product_blueprint.get("/export_products/<id>")
    def export_products(id):
        try:
            result = ProductService.export_products_by_event_id(id)

            return send_file(result), 200
        except CustomError as e:
            return e.to_response()
        except:
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403
        
    @product_blueprint.put("/import_products/<id>")
    def import_products(id):
        try:
            result = ProductService.import_products_to_event(id, request.files)

            return [e.toJson() for e in result], 200
        except CustomError as e:
            return e.to_response()
        except Exception as e:
            print(e)
            return {
                'code': 1,
                'message': 'Ocorreu um erro'
            }, 403