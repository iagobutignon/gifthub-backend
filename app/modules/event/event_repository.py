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
    
    def getEventsByUserId(id):
        aux = []
        for e in events:
            if e.userId == id:
                aux.append(e)
        
        return aux

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
        event.description = eventModel.description or event.description
        event.date = eventModel.date or event.date
        event.time = eventModel.time or event.time
        event.image = eventModel.image or event.image
        event.address = eventModel.address or event.address

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

        return event