import json
from app.modules.product.product_model import ProductModel

from app.modules.product.product_repository import ProductRepository


class ProductService:
    def export_products_by_event_id(event_id):
        result = ProductRepository.get_products_by_event_id(event_id)

        data = {
            "products" : [e.export() for e in result]
        }

        temp_file_path = './temp/export_' + event_id + '.json'
        with open(temp_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return temp_file_path
    
    def import_products_to_event(event_id, request_files):
        try:
            print(request_files)
            if 'file' not in request_files:
                return 'Nenhum arquivo recebido', 400
                
            file = request_files['file']

            file_path = './temp/' + file.filename
            file.save(file_path)
            
            with open(file_path, 'r') as arquivo_json:
                data = json.load(arquivo_json)

            products = []
            for p in data['products']:
                p['event_id'] = event_id
                product = ProductModel(p)
                products.append(product)

            ProductRepository.create_products(products)
            
            result = []
            for p in products:
                result.append(ProductRepository.get_product_by_id(p.id))
            
            return result
        except Exception as e:
            print(e)