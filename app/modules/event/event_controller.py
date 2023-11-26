from flask import Blueprint, request


event_blueprint = Blueprint("event", __name__)


class EventController():
    @event_blueprint.post("/create_event")
    def create_event(self):
        data = request.get_json()

        return data, 200

    @event_blueprint.post("/edit_event")
    def edit_event(self):
        data = request.get_json()

        return data, 200

    @event_blueprint.post("/delete_event")
    def delete_event():
        data = request.get_json()

        return data, 200
    
    @event_blueprint.post("/get_event")
    def get_event():
        data = request.get_json()

        return data, 200
    
    @event_blueprint.post("/list_events")
    def list_events():
        data = request.get_json()

        return data, 200