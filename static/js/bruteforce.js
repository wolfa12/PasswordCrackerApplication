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
    var lengthparam = document.forms["bruteforceform"]["lengthparam"].value;
    console.log("char set is     :"+charset)
    if (accusername == "" || charset == "" || lengthparam == "") {
        alert("Please fill out all fields");
        return false;
    }
    }