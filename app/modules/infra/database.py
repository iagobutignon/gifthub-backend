database = None
engine = None

def configure_database(app):
    global engine

    app.config["SQL_ALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://fabrico:fabrico123@localhost/database_db_1'
    app.config["SQL_ALCHEMY_TRACK_MODIFICATIONS"] = False


def read_file(file):
    with open(file, 'r') as file:
        return file.read()