# Handler to get attendees for given event. Returns JSON.

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import lwc.data

class GetAttendees(webapp.RequestHandler):
  def get(self):
    event_id = self.request.get('eid', None)
    attendees_str = ''
    
    if event_id:
      user_events = lwc.data.fetch_event_attendees(event_id)
      if user_events:
        first = True
        for user_event in user_events:
          if first:
            first = False
          else:
            attendees_str += ','
          attendees_str += str(user_event.user_id)
    
    response = '{attendees:[' + attendees_str + ']}'
    self.response.out.write(response)

application = webapp.WSGIApplication(
                                     [('/get_attendees', GetAttendees)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()