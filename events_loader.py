# Loader class to describe data translation for uploading events into 
# App Engine data store.

import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader
import lwc.models

class EventsLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Events', 
                                   [('id', int),
                                    ('timestamp', 
                                     lambda x: datetime.datetime.fromtimestamp(float(x))),
                                    ('facebook_event', bool),
                                    ('title', str),
                                    ('description', str),
                                    ('location', str),
                                    ('moderators', str),
                                    ('panelists', str)
                                   ])

loaders = [EventsLoader]