from app.modules.shared.errors import Errors
from app.modules.infra.database import database
from app.modules.event.event_model import EventModel

class EventRepository:
    def get_events():
        events = EventModel.query.all()

        return events
    
    def get_event_by_id(id):
        event = EventModel.query.filter_by(id=id).first()

        if event == None:
            raise Errors.event_not_found()
        
        return event
    
    def get_events_by_user_id(id):
        events = EventModel.query.filter_by(user_id=id)

        return events

    def create_event(event_model):
        try:
            database.session.add(event_model)
            database.session.commit()

            return event_model
        except:
            raise Errors.error_creating_event()
        
    def update_event(id, event_model):
        event = EventModel.query.filter_by(id=id).first()
        
        if event == None:
            raise Errors.event_not_found()

        event.name = event_model.name or event.name
        event.description = event_model.description or event.description
        event.date = event_model.date or event.date
        event.time = event_model.time or event.time
        event.picture = event_model.picture or event.picture
        event.cep = event_model.cep or event.cep
        event.number = event_model.number or event.number
        event.street = event_model.street or event.street
        event.district = event_model.district or event.district
        event.city = event_model.city or event.city
        event.state = event_model.state or event.state
        event.complement = event_model.complement or event.complement

        database.session.commit()

        return event
    
    def delete_event(id):
        event = EventModel.query.filter_by(id=id).first()

        if event == None:
            raise Errors.event_not_found()
        
        database.session.delete(event)
        database.session.commit()

        return event