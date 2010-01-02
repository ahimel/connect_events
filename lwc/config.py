# Config settings for site. The intention is that only this file sould have
# to be modified for setting up a new Connect-enabled events site.

from datetime import datetime
import timezones

FACEBOOK_API_KEY = 'YOUR API KEY'
FACEBOOK_SECRET_KEY = 'YOUR SECRET KEY'
SITE_NAME = 'Le Web Connect'
DAY_TABS = {'day1' : {'label' : 'Dec 9',
                      'start' : datetime(2009, 12, 9, 8, 0, 0, 0, 
                                         timezones.paris_time),
                      'end' :   datetime(2009, 12, 9, 23, 59, 59, 59, 
                                         timezones.paris_time)},
            'day2' : {'label' : 'Dec 10',
                      'start' : datetime(2009, 12, 10, 8, 0, 0, 0, 
                                         timezones.paris_time),
                      'end' :   datetime(2009, 12, 10, 23, 59, 59, 59, 
                                         timezones.paris_time)}}
DEFAULT_TAB = 'day1'
