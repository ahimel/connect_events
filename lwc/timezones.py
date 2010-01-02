from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)
HOUR = timedelta(hours=1)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO

  def tzname(self, dt):
    return "UTC"

  def dst(self, dt):
    return ZERO

utc = UTC()

class ParisTime(tzinfo):
  def utcoffset(self, dt):
    return HOUR
  
  def tzname(self, dt):
    return 'CET'
    
  def dst(self, dt):
    return ZERO
    
paris_time = ParisTime()