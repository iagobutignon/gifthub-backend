import mariadb

from app.modules.infra.database import configure_database
from flask import Flask
from app.modules.auth.auth_controller import auth_blueprint
from app.modules.profile.profile_controller import profile_blueprint
from app.modules.event.event_controller import event_blueprint
from app.modules.product.product_controller import product_blueprint

conn = mariadb.connect(
    user="root",
    password="fabrico123",
    host="localhost",
    port=3306,
    database="banco_do_fabrico",
)

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(profile_blueprint, url_prefix="/profile")
app.register_blueprint(event_blueprint, url_prefix="/event")
app.register_blueprint(product_blueprint, url_prefix="/product")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
