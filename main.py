from app.modules.infra.database import configure_database
from flask import Flask
from app.modules.user.user_controller import user_blueprint
from app.modules.event.event_controller import event_blueprint
from app.modules.product.product_controller import product_blueprint
from app.modules.address.address_controller import address_blueprint
from flask_cors import CORS

app = Flask(__name__)
configure_database(app)
CORS(app, resources={r"/": {"origins": ""}}, supports_credentials=True)

app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(event_blueprint, url_prefix="/event")
app.register_blueprint(product_blueprint, url_prefix="/product")
app.register_blueprint(address_blueprint, url_prefix="/address")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
