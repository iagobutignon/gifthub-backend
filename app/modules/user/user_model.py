import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID
from app.modules.infra.database import database


class UserModel(database.Model):
    __tablaname__ = 'users'

    id = database.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    email = database.Column(
        database.String(100),
        unique=True,
        nullable=False
    )
    password = database.Column(
        database.String(100),
        nullable=False
    )
    name = database.Column(
        database.String(100),
        nullable=False
    )
    surname = database.Column(
        database.String(100),
        nullable=False
    )
    description = database.Column(
        database.String(255),
        nullable=False
    )
    cep = database.Column(
        database.String(9),
        nullable=False
    )
    number = database.Column(
        database.String(10),
        nullable=False
    )
    street = database.Column(
        database.String(50),
        nullable=False
    )
    district = database.Column(
        database.String(50),
        nullable=False
    )
    city = database.Column(
        database.String(50),
        nullable=False
    )
    state = database.Column(
        database.String(2),
        nullable=False
    )
    complement = database.Column(
        database.String(50),
        nullable=False
    )
    created_at = database.Column(
        database.DateTime,
        default=datetime.datetime.now(),
        nullable=False
    )
    updated_at = database.Column(
        database.DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        nullable=False
    )

    def __init__(self, data):
        self.email = data['email']
        self.password = data['password']
        self.name = data['name']
        self.surname = data['surname']
        self.description = data['description']
        self.cep = data['cep']
        self.number = data['number']
        self.street = data['street']
        self.district = data['district']
        self.city = data['city']
        self.state = data['state']
        self.complement = data['complement']
        
    def toJson(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'description': self.description,
            'cep': self.cep,
            'number': self.number,
            'street': self.street,
            'district': self.district,
            'city': self.city,
            'state': self.state,
            'complement': self.complement,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }