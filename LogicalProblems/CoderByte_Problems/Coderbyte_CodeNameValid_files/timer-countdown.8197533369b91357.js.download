function __parseTimeFromString(str){if(str.indexOf(':')!==-1){var parsed=str.split(':');return[parseInt(parsed[0]),parseInt(parsed[1])]}
if(str.indexOf('hours')!==-1){var str=str.replace('hours','');str=str.replace('minutes','');parsed=str.split(',');return[parseInt(parsed[0]),parseInt(parsed[1])]}}
function __subtractMinute(parsedTime){var hours=parseInt(parsedTime[0]);var minutes=parseInt(parsedTime[1]);minutes=minutes-1;if(minutes<0){hours=hours-1;minutes=59}
return[hours,minutes]}
function __displayNewTime(parsed,timerAreaElement){if(typeof parsed==='object'){timerAreaElement.innerHTML=(parsed[0]+' hours, '+parsed[1]+' minutes')}}
function __showTimerMessage(message,timerClassString){var timerAreaElement=document.getElementsByClassName(timerClassString)[0];timerAreaElement.innerHTML=message}
function __beginTimer(timerString,timerClassString){if(!timerString||timerString===''){__showTimerMessage('Unlimited time',timerClassString);return}
var timerAreaElement=document.getElementsByClassName(timerClassString)[0];var parsed=__parseTimeFromString(timerString);__displayNewTime(parsed,timerAreaElement);setInterval(function(){var parsed=__parseTimeFromString(timerAreaElement.innerHTML);var newTime=__subtractMinute(parsed);if(newTime[0]<0){window.location.replace('/candidate-assessment')}
__displayNewTime(newTime,timerAreaElement)},60000)}