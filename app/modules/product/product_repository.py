from app.modules.shared.errors import Errors
from app.modules.infra.database import products

class ProductRepository:
    def getProducts():
        return products

    def getProductById(id):
        for p in products:
            if p.id == id:
                return p
    
        raise Errors.productNotFound()
    
    def createProduct(productModel):
        products.append(productModel)
            
        return productModel
    
    def updateProduct(id, productModel):
        product = None
        for p in products:
            if p.id == id:
                product = p
                break
        
        if product == None:
            raise Errors.productNotFound()
        
        product.name = productModel.name or product.name

        return product
    
    def deleteProduct(id):
        product = None
        for p in products:
            if p.id == id:
                product = p
                break
        
        if product == None:
            raise Errors.productNotFound()
        
        products.remove(product)