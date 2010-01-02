# Data Access Layer for user and event data from App Engine data store

import models
import uievent

from google.appengine.ext import db

# Retrieve user ids attending a given event
def fetch_event_attendees(event_id):
  query = 'SELECT * FROM UserEvents WHERE event_id = :1'
  attendees = db.GqlQuery(query, event_id)
  return attendees

# Retrieve events with metadata for given start and end datatime objects
def fetch_events_day(start, end):
  query = 'SELECT * FROM Events WHERE timestamp >= :1 AND timestamp <= :2'
  query += ' ORDER BY timestamp ASC'
  events = db.GqlQuery(query, start, end)
  return _populate_events(events)

# Retrieve events hosted by Facebook
def fetch_events_facebook():
  query = 'SELECT * FROM Events WHERE facebook_event = True'
  query += ' ORDER BY timestamp ASC'
  events = db.GqlQuery(query)
  return _populate_events(events)

# Retrieve events attended by given user ids
def fetch_events_friends(friend_ids):
  chunk_size = 30 #imposed by app engine
  range_list = range(0, len(friend_ids), chunk_size)
  chunked_friends = [friend_ids[i:i+chunk_size] for i in range_list]
  events = list()
  query = 'SELECT * FROM UserEvents WHERE user_id in :1'
  for chunk_list in chunked_friends:
    friend_events = db.GqlQuery(query, chunk_list)
    if friend_events:
      for event in friend_events:
        events.append(db.get(event.event_id))
  return _populate_events(events)

# Retrieve events attended by given user
def fetch_events_mine(fbuser):
  if fbuser:
    query = 'SELECT * FROM UserEvents WHERE user_id = :1'
    my_events = db.GqlQuery(query, int(fbuser))
    if my_events:
      events = list()
      for event in my_events:
        events.append(db.get(event.event_id))
      return _populate_events(events)

  return list()

# Convert raw event into format expected by UI renderers
def _populate_events(events):
  renderable_events = list()
  for event in events:
    attendees = fetch_event_attendees(str(event.key()))
    renderable_event = uievent.RenderableEvent(event, attendees)
    renderable_events.append(renderable_event)

  return renderable_events
