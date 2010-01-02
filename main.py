# Request handler for rendering all pages in this site.

import cgi
import os
import lwc.data
import lwc.ui
from lwc.state import State

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self):
    # Initialize state from config
    State.init(self)
    fb = State.get_facebook()
    fbuser = State.get_facebook_user()
    
    # Show Facebook profile pic if logged into FB Connect
    profile_pic = None
    if fbuser:
      q = 'SELECT pic_small_with_logo FROM user where uid=' + str(fbuser)
      res = fb.fql.query(q)
      profile_pic = res[0][u'pic_small_with_logo']
      if not profile_pic:
        profile_pic = 'http://static.ak.fbcdn.net/pics/t_silhouette_logo.gif'
    
    # User agent for some CSS casing
    body_class = ''
    useragent = self.request.headers['user-agent']
    if useragent.find('ie') >= 0:
      body_class = ' class=\'ie6\''
    
    # tabs
    tabs_content = ''
    tabs = State.get_tabs()
    selected = State.get_selected()
    first = True
    for tab_key, tab_value in sorted(tabs.iteritems()):
      li_class = ''
      if first:
        li_class = ' class=\'first\''
        first = False
      
      a_class = ''
      if tab_key == selected:
        a_class = ' class=\'selected\''
          
      tabs_content += '<li' + li_class + '>';
      tabs_content += '<a' + a_class + ' href=\'/?tab=' + tab_key + '\'>'
      tabs_content += tab_value['label'] + '</a>';
      tabs_content += '</li>'
    
    # events
    event_data = None
  
    if selected == 'fb':
      event_data = lwc.data.fetch_events_facebook()
    elif selected == 'friends':
      if fbuser:
        friend_ids = fb.friends.get()
        event_data = lwc.data.fetch_events_friends(friend_ids)
    elif selected == 'mine':
      event_data = lwc.data.fetch_events_mine(fbuser)
    else:
      tab_config = tabs[selected]
      event_data = lwc.data.fetch_events_day(tab_config['start'], 
                                             tab_config['end'])
    
    events_content = ''
    if event_data:
      for event in event_data:
        events_content += lwc.ui.render_event(event, fbuser)
    
    # render template
    template_values = {
      'site_name' : State.get_site_name(),
      'body_class' : body_class,
      'profile_pic' : profile_pic,
      'tabs_content' : tabs_content,
      'events_content': events_content
    }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))
    
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()