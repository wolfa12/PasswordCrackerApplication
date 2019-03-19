$(document).ready(function(){
  $("#numberscheck").click(function(){
   $("#setofchar").val(function(i, origText){
    return origText + "1234567890";
  });
  });
    $("#letterscheck").click(function(){
   $("#setofchar").val(function(i, origText){
    return origText + "abcdefghijklmnopqrstuvwxyz";
  });
  });
    $("#specialcharcheck").click(function(){
   $("#setofchar").val(function(i, origText){
    return origText + "!@#$%^&*(){}[]+=_-:;'?/>.<,"+'"';
  });
  });

});
function validateform() {
    var accusername = document.forms["bruteforceform"]["accusername"].value;
    var charset = document.forms["bruteforceform"]["charset"].value;
    var pl1 = document.forms["bruteforceform"]["passwordlength1"].value;
    var pl2 = document.forms["bruteforceform"]["passwordlength2"].value;
    console.log("min length     :"+pl1)
    console.log("max length     :"+pl2)
    if (accusername == "" || charset == "") {
        alert("Please fill out all fields");
        return false;
    } else if(pl1>pl2){
        alert("Password minimum length must be less than password maximum length")
        return false;
    }
    }