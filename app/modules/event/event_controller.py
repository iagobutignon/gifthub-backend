from flask import Blueprint, request
from app.modules.event.event_model import EventModel

from app.modules.event.event_repository import EventRepository


event_blueprint = Blueprint("event", __name__)


class EventController():    
    @event_blueprint.get("/")
    def get_events():
        try:
            result = EventRepository.getEvents()

            return [e.toJson() for e in result], 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]
    
    @event_blueprint.get("/get_events_by_user_id/<id>")
    def get_events_by_user_id(id):
        try:
            result = EventRepository.getEventsByUserId(id)
            
            return [e.toJson() for e in result], 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }. e.args[2]
        
    @event_blueprint.get("/<id>")
    def get_event(id):
        try:
            result = EventRepository.getEventById(id)
            
            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]

    @event_blueprint.post("/")
    def create_event():
        try:
            data = request.get_json(force=True,silent=True)
            event = EventModel(data)
            result = EventRepository.createEvent(event)

            return result.toJson(), 201
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]


    @event_blueprint.put("/<id>")
    def edit_event(id):
        try:
            data = request.get_json()
            event = EventModel(data)
            result = EventRepository.updateEvent(id, event)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]


    @event_blueprint.delete("/<id>")
    def delete_event(id):
        try:
            result = EventRepository.deleteEvent(id)

            return result.toJson(), 200
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }, e.args[2]