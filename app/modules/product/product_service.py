import json

from app.modules.product.product_repository import ProductRepository


class ProductService:
    def export_products_by_event_id(event_id):
        result = ProductRepository.get_products_by_event_id(event_id)

        data = {
            "event_id": event_id,
            "products" : [e.export() for e in result]
        }

        temp_file_path = './temp/export_' + event_id + '.json'
        with open(temp_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return temp_file_path