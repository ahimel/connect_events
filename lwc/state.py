from facebook import Facebook
import config

class State():
  _selected = None
  _tabs = None
  _facebook = None
  _facebook_user = None
    
  @staticmethod
  def init(webhandler):
    State._tabs = {'fb'      : {'label' : 'Facebook Events'},
                   'friends' : {'label' : 'Friends\' Events'},
                   'mine'    : {'label' : 'My Events'}}
    for day_tab in config.DAY_TABS:
      State._tabs[day_tab] = config.DAY_TABS[day_tab]
    
    State._selected = webhandler.request.get('tab', config.DEFAULT_TAB)

    fb = Facebook(config.FACEBOOK_API_KEY, config.FACEBOOK_SECRET_KEY)
    fb.check_session(webhandler.request)
    
    State._facebook = fb
    State._facebook_user = fb.uid
    
  @staticmethod
  def get_site_name():
    return config.SITE_NAME
  
  @staticmethod
  def get_selected():
    return State._selected
      
  @staticmethod
  def get_tabs():
    return State._tabs
  
  @staticmethod
  def get_facebook():
    return State._facebook
  
  @staticmethod
  def get_facebook_user():
    return State._facebook_user
  