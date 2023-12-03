users = []
events = []
products = []

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

database = SQLAlchemy()
engine = None

def configure_database(app):
    global engine

    db_url = "postgresql://fabrico:fabrico123@172.21.0.2:5432/banco_do_fabrico"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    engine = create_engine(db_url)
    database.init_app(app)

    with app.app_context():
        database.create_all()
