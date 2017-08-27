function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function pad(number){
  return (number < 10) ? "0" + number : number
}

function getCurrentTime(){  
  var currentTime = new Date()
  var month = currentTime.getMonth() + 1
  var day = currentTime.getDate()
  var year = currentTime.getFullYear()
  var hours = currentTime.getHours()
  var minutes = pad(currentTime.getMinutes())
  var seconds = pad(currentTime.getSeconds())
  return month + "/" + day + "/" + year + " " + hours + ":" + minutes + ":" + seconds
}

window.onload = function(){
  document.getElementById('last_modified_time').innerHTML = "Schedule as of : " + getCurrentTime()
}