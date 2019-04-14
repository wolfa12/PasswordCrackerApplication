$(document).ready(function(){
  var originDict = $('#dictionary').val();
  $('#restart').click(function(){
      $('#dictionary').val(originDict)
  })
});
function validateform(){
    var password = document.forms["passwordform"]["password"].value;
    if (password == "") {
        alert("Please fill out all fields");
        return false;
    }
    if(password.indexOf(' ') >= 0){
        alert("Password must not contain spaces!")
    }
}