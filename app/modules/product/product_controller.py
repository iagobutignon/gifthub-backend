from flask import Blueprint, request


product_blueprint = Blueprint("product", __name__)


class ProductController():
    @product_blueprint.post("/create_product")
    def create_product(self):
        data = request.get_json()

        return data, 200

    @product_blueprint.post("/edit_product")
    def edit_product(self):
        data = request.get_json()

        return data, 200

    @product_blueprint.post("/delete_product")
    def delete_product():
        data = request.get_json()

        return data, 200

    @product_blueprint.post("/get_product")
    def get_product():
        data = request.get_json()

        return data, 200

    @product_blueprint.post("/list_products")
    def list_products():
        data = request.get_json()

        return data, 200
