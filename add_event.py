# Handler for toggling attendance status of user/event pair.

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from lwc.models import UserEvents

class AddEvent(webapp.RequestHandler):
  def post(self):
    success = False
    
    user_id = self.request.get('uid', None)
    event_id = self.request.get('eid', None)
    attend = self.request.get('attend', False)

    if user_id and event_id:
      user_event = UserEvents()
      user_event.user_id = int(user_id)
      user_event.event_id = event_id
      if user_event.put():
        success = True

    success_str = success and "1" or "0"
    attend_str = attend and "1" or "0"
    result = '{success: ' + success_str + ', attend: ' + attend_str + '}'
    self.response.out.write(result)
  
application = webapp.WSGIApplication(
                                     [('/add_event', AddEvent)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()