$(document).ready(function(){
  var calculateCombos = function(){
    var minpasslength = $("#passwordlength1").val();
    var maxpasslength = $("#passwordlength2").val();
    var charsetLength = $("#setofchar").val().length;
    if(maxpasslength<minpasslength){
      alert("Maximum length must be greater than minimum length")
    } else{
      var total = 0;
      while(minpasslength<=maxpasslength){
        total+=Math.pow(charsetLength, minpasslength)
        minpasslength++;
      }
      $("#combos").text("Number of Combinations: "+total);
    }
    
  }
  $("#numberscheck").click(function(){
   $("#setofchar").val(function(i, origText){
    return origText + "1234567890";
  });
  calculateCombos()
  });
    $("#letterscheck").click(function(){
   $("#setofchar").val(function(i, origText){
    return origText + "abcdefghijklmnopqrstuvwxyz";
  });
  calculateCombos();
  });
    $("#specialcharcheck").click(function(){
      $("#setofchar").val(function(i, origText){
        return origText + "!@#$%^&*(){}[]+=_-:;'?/>.<,"+'"';
      });
      calculateCombos();
  });
  $("#passwordlength1").change(calculateCombos);
  $("#passwordlength2").change(calculateCombos);
  $("#setofchar").change(calculateCombos)
});
function validateform() {
    var accusername = document.forms["bruteforceform"]["accusername"].value;
    var charset = document.forms["bruteforceform"]["charset"].value;
    var pl1 = document.forms["bruteforceform"]["passwordlength1"].value;
    var pl2 = document.forms["bruteforceform"]["passwordlength2"].value;
    if (accusername == "" || charset == "") {
        alert("Please fill out all fields");
        return false;
    } else if(pl1>pl2){
        alert("Password minimum length must be less than password maximum length")
        return false;
    }
    }