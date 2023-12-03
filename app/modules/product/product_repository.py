from app.modules.shared.errors import Errors
from app.modules.infra.database import database
from app.modules.product.product_model import ProductModel

class ProductRepository:
    def get_products():
        products = ProductModel.query.all()

        return products
    
    def get_product_by_id(id):
        product = ProductModel.query.filter_by(id=id).first()

        if product == None:
            raise Errors.product_not_found()
        
        return product

    def get_products_by_event_id(id):
        products = ProductModel.query.filter_by(event_id=id)

        return products
    
    def create_product(product_model):
        try:
            database.session.add(product_model)
            database.session.commit()

            return product_model
        except:
            raise Errors.error_creating_product()
    
    def update_product(id, product_model):
        product = ProductModel.query.filter_by(id=id).first()
        
        if product == None:
            raise Errors.product_not_found()
        
        product.picture = product_model.picture or product.picture
        product.name = product_model.name or product.name
        product.value = product_model.value or product.value
        product.description = product_model.description or product.description

        database.session.commit()

        return product
    
    def delete_product(id):
        product = ProductModel.query.filter_by(id=id).first()

        if product == None:
            raise Errors.product_not_found()
        
        database.session.delete(product)
        database.session.commit()

        return product