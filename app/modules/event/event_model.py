import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID
from app.modules.infra.database import database


class EventModel(database.Model):
    __tablaname__ = 'events'

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
        self.userId = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.date = data['date']
        self.time = data['time']
        self.image = data['image']
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
            'user_id': self.userId,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'time': self.time,
            'image': self.image,
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