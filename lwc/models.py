# Data model for events and user/event attendance

from google.appengine.ext import db

class Events(db.Model):
  timestamp = db.DateTimeProperty()
  facebook_event = db.BooleanProperty()
  title = db.StringProperty()
  description = db.StringProperty(None, True)
  location = db.StringProperty()
  moderators = db.StringProperty(None, True)
  panelists = db.StringProperty(None, True)

class UserEvents(db.Model):
  timestamp = db.DateTimeProperty(None, True)
  user_id = db.IntegerProperty()
  event_id = db.StringProperty()