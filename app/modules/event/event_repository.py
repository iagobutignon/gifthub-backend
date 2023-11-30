from app.modules.shared.errors import Errors
from app.modules.infra.database import events


class EventRepository:
    def getEvents():
        return events
    
    def getEventById(id):
        for e in events:
            if e.id == id:
                return e
    
        raise Errors.eventNotFound()
    
    def createEvent(eventModel):
        events.append(eventModel)
            
        return eventModel
    
    def updateEvent(id, eventModel):
        event = None
        for e in events:
            if e.id == id:
                event = e
                break
        
        if event == None:
            raise Errors.eventNotFound()
        
        event.name = eventModel.name or event.name

        return event
    
    def deleteEvent(id):
        event = None
        for e in events:
            if e.id == id:
                event = e
                break
        
        if event == None:
            raise Errors.eventNotFound()
        
        events.remove(event)