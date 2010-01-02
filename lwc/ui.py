def render_event(renderable_event, fbuser):
  event = renderable_event.event
  attendees = renderable_event.attendees
  user_attending = False
  if fbuser:
    for user_event in attendees:
      if int(fbuser) == user_event.user_id:
        user_attending = True
        break

  html = '<div class=\'timeline\'>'
  html += event.timestamp.strftime("%b %d %I:%M %p")
  html += '</div>'
  html += '<div class=\'partyrow\'>'
  html += '<table cellspacing=\'0\' cellpadding=\'0\' border=\'0\''
  html += ' width=\'100%\'>'
  html += '<tr>'

  if event.facebook_event:
    html += '<td class=\'tunaimage\'>'
    html += '<img alt=\'\' src=\'/images/fb_logo.png\'/>'
    html += '</td>'

  html += '<td class=\'info\'>'
  html += '<table cellspacing=\'0\' cellpadding=\'0\' border=\'0\''
  html += ' width=\'96%\' class=\'infotable\'>'
  html += '<tr>'
  html += '<td colspan=\'2\' class=\'eventtitle\'>'
  html += '<h3>' + event.title + '</h3>'
  html += '</td>'
  html += '</tr>'

  if event.description != '':
    html += '<tr valign=\'top\'>'
    html += '<td colspan=\'2\'>' + event.description + '</td>'
    html += '</tr>'

  if event.moderators != '':
    html += '<tr valign=\'top\'>'
    html +='<td class=\'label\'>Moderated by:</td>'
    html += '<td>' + event.moderators + '</td>'
    html += '</tr>'

  if event.panelists != '':
    html += '<tr valign=\'top\'>'
    html += '<td class=\'label\'>Panelists:</td>'
    html += '<td>' + event.panelists + '</td>'
    html += '</tr>'

  html += '<tr valign=\'top\'>'
  html += '<td class=\'label\'>Location:</td>'
  html += '<td>' + event.location + '</td>'
  html += '</tr>'

  html += '</table></td>'

  if fbuser:
    label = user_attending and 'Not Attending' or 'Attend'
    html += '<td class=\'actions\' nowrap=\'nowrap\'>'
    html += '<a id=\'attend_' + str(event.key()) + '\''
    html += ' onclick=\'attend_event("' + str(event.key()) + '");\'>' + label
    html += '</a>'
    html += '<a onclick=\'show_attendees("' + str(event.key()) + '");\'>'
    html += 'View Guest List</a>'
    html += '</td>'

  html += '</tr></table></div>'

  return html
