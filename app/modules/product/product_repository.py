from app.modules.shared.errors import Errors
from app.modules.infra.database import products

class ProductRepository:
    def get_products():
        return products

    def get_product_by_id(id):
        for p in products:
            if p.id == id:
                return p
    
        raise Errors.product_not_found()

    def get_products_by_event_id(id):
        aux = []
        for p in products:
            if p.eventId == id:
                aux.append(p)
        
        return aux
    
    def create_product(productModel):
        products.append(productModel)
            
        return productModel
    
    def update_product(id, productModel):
        product = None
        for p in products:
            if p.id == id:
                product = p
                break
        
        if product == None:
            raise Errors.product_not_found()
        
        product.picture = productModel.picture or product.picture
        product.name = productModel.name or product.name
        product.value = productModel.value or product.value
        product.description = productModel.description or product.description

        return product
    
    def delete_product(id):
        product = None
        for p in products:
            if p.id == id:
                product = p
                break
        
        if product == None:
            raise Errors.product_not_found()
        
        products.remove(product)

        return product