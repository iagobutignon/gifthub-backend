import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID, DATE, TIME, TEXT
from app.modules.infra.database import database


class EventModel(database.Model):
    __tablaname__ = 'events'

    id = database.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )
    user_id = database.Column(
        UUID(as_uuid=True),
        database.ForeignKey("user_model.id"),
        nullable=False
    )
    name = database.Column(
        database.String(100),
        nullable=False
    )
    description = database.Column(
        database.String(255),
        nullable=False
    )
    date = database.Column(
        DATE,
        nullable=False
    )
    time = database.Column(
        TIME,
        nullable=False
    )
    picture = database.Column(
        TEXT,
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
    user = database.relationship("UserModel")

    def __init__(self, data):
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.date = data['date']
        self.time = data['time']
        self.picture = data['picture']
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
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'date': str(self.date),
            'time': str(self.time),
            'picture': self.picture,
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