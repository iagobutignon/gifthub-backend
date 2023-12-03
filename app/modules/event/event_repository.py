from app.modules.shared.errors import Errors
from app.modules.infra.database import events


class EventRepository:
    def get_events():
        return events
    
    def get_event_by_id(id):
        for e in events:
            if e.id == id:
                return e
    
        raise Errors.event_not_found()
    
    def get_events_by_user_id(id):
        aux = []
        for e in events:
            if e.userId == id:
                aux.append(e)
        
        return aux

    def create_event(eventModel):
        events.append(eventModel)
            
        return eventModel
    
    def update_event(id, eventModel):
        event = None
        for e in events:
            if e.id == id:
                event = e
                break
        
        if event == None:
            raise Errors.event_not_found()
        
        event.name = eventModel.name or event.name
        event.description = eventModel.description or event.description
        event.date = eventModel.date or event.date
        event.time = eventModel.time or event.time
        event.picture = eventModel.picture or event.picture
        event.address = eventModel.address or event.address

        return event
    
    def delete_event(id):
        event = None
        for e in events:
            if e.id == id:
                event = e
                break
        
        if event == None:
            raise Errors.event_not_found()
        
        events.remove(event)

        return event