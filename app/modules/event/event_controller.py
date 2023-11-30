from flask import Blueprint, request


event_blueprint = Blueprint("event", __name__)


class EventController():    
    @event_blueprint.get("/")
    def get_events():
        try:
            None
            # TODO: Implementar get_events
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }    

    @event_blueprint.get("/<id>")
    def get_event(id):
        try:
            None
            # TODO: Implementar get_event
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }

    @event_blueprint.post("/")
    def create_event():
        try:
            None
            # TODO: Implementar create_event
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }


    @event_blueprint.put("/<id>")
    def edit_event(id):
        try:
            None
            # TODO: Implementar edit_event
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }


    @event_blueprint.delete("/<id>")
    def delete_event(id):
        try:
            None
            # TODO: Implementar delete_event
        except Exception as e:
            return {
                'code': e.args[0],
                'message': e.args[1],
                'statusCode': e.args[2]
            }