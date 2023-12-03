import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID, TEXT, NUMERIC
from app.modules.infra.database import database


class ProductModel(database.Model):
    __tablaname__ = 'products'

    id = database.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    event_id = database.Column(
        UUID(as_uuid=True),
        database.ForeignKey("event_model.id"),
        nullable=False
    )
    picture = database.Column(
        TEXT,
        nullable=False
    )
    name = database.Column(
        database.String(100),
        nullable=False
    )
    value = database.Column(
        NUMERIC,
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
    event = database.relationship("EventModel")

    def __init__(self, data):
        self.event_id = data['event_id']
        self.picture = data['picture']
        self.name = data['name']
        self.value = data['value']
        self.description = data['description']

    def toJson(self):
        return {
            'id': str(self.id),
            'event_id': self.event_id,
            'picture': self.picture,
            'name': self.name,
            'value': self.value,
            'description': self.description,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }