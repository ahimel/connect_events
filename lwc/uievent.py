class RenderableEvent:
  _event = None
  _attendees = None
  
  def __init__(self, event, attendees):
    self._event = event
    self._attendees = attendees
  
  @property
  def event(self):
    return self._event
  
  @property
  def attendees(self):
    return self._attendees