from flask import Blueprint, request
from app.modules.event.event_model import EventModel

from app.modules.event.event_repository import EventRepository
from app.modules.shared.custom_error import CustomError


event_blueprint = Blueprint("event", __name__)


class EventController():    
    @event_blueprint.get("/")
    def get_events():
        try:
            result = EventRepository.get_events()

            return [e.toJson() for e in result], 200
        except CustomError as e:
            return e.to_response()
    
    @event_blueprint.get("/get_events_by_user_id/<id>")
    def get_events_by_user_id(id):
        try:
            result = EventRepository.get_events_by_user_id(id)
            
            return [e.toJson() for e in result], 200
        except CustomError as e:
            return e.to_response()
        
    @event_blueprint.get("/<id>")
    def get_event(id):
        try:
            result = EventRepository.get_event_by_id(id)
            
            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()

    @event_blueprint.post("/")
    def create_event():
        try:
            data = request.get_json(force=True,silent=True)
            event = EventModel(data)
            result = EventRepository.create_event(event)

            return result.toJson(), 201
        except CustomError as e:
            return e.to_response()


    @event_blueprint.put("/<id>")
    def update_event(id):
        try:
            data = request.get_json()
            event = EventModel(data)
            result = EventRepository.update_event(id, event)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()


    @event_blueprint.delete("/<id>")
    def delete_event(id):
        try:
            result = EventRepository.delete_event(id)

            return result.toJson(), 200
        except CustomError as e:
            return e.to_response()