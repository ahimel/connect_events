function show_attendees(event_id) {
  var attendeesDom = document.createElement('div');
  attendeesDom.className = 'attendees_content';
  attendeesDom.id = 'attendees_' + event_id;
  var dialog = new FB.UI.PopupDialog('View Guest List',
                                     attendeesDom,
                                     false,
                                     false);
  dialog.show();
  
  var request = get_xmlhttprequest();
  if (request) {
    request.open('GET', '/get_attendees?eid=' + event_id, true);
    
    request.onreadystatechange = function() {
      if (request.readyState == 4 && request.status == 200) {
        var response = eval('(' + request.responseText + ')');
        var attendees = response.attendees;
        var markup = '<table cellspacing="5">';
        for (var i in attendees) {
          markup += '<tr><td>';
          markup += '<fb:profile-pic uid="' + attendees[i] + '" size="thumb"';
          markup += ' facebook-logo="true"></fb:profile-pic>';
          markup += '</td><td>';
          markup += '<fb:name uid="' + attendees[i] + '" useyou="false"'
          markup += ' linked="true"></fb:name>';
          markup += '</td></tr>';
        }
        
        markup += '</table>';
        var attendeesDom = document.getElementById('attendees_' + event_id);
        attendeesDom.innerHTML = markup;
        FB.XFBML.Host.parseDomElement(attendeesDom);
      }
    };
    
    request.send(null);
  }
}

function attend_event(event_id) {
  var attend = '1';
  var attend_dom = document.getElementById('attend_' + event_id);
  if (attend_dom.innerHTML.substr(0,1) == 'D') {
    attend = '0';
  }
  
  var params = 'uid=' + FB.Connect.get_loggedInUser() + '&eid=' + event_id;
  params += '&attend=' + attend;
  var request = get_xmlhttprequest();
  if (request) {
    request.open('POST', '/add_event', true);
    request.setRequestHeader('uid', FB.Connect.get_loggedInUser());
    request.setRequestHeader('eid', event_id);
    
    request.onreadystatechange = function() {
      if (request.readyState == 4 && request.status == 200) {
        handle_add_event(event_id, eval('(' + request.responseText + ')'));
      }
    };
    
    request.setRequestHeader('Content-type', 
                             'application/x-www-form-urlencoded');
    request.setRequestHeader('Content-length', params.length);
    request.send(params);
  }
}

function handle_add_event(event_id, response) {
  if (response.success) {
    var str = response.attend ? 'Not Attending' : 'Attend';
    var id = 'attend_' + event_id;
    document.getElementById(id).innerHTML = str;
  }
}

function get_xmlhttprequest() {
  var transport = null;

  try {
    transport = new XMLHttpRequest();
  } catch (ignored) {};

  if (!transport) {
    try {
      transport = new ActiveXObject('Msxml2.XMLHTTP');
    } catch (ignored) {};
  }

  if (!transport) {
    try {
      transport = new ActiveXObject('Microsoft.XMLHTTP');
    } catch (ignored) {};
  }
  
  return transport;
}