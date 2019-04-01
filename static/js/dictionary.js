$(document).ready(function(){
  var originDict = $('#dictionary').val();
  $('#restart').click(function(){
      $('#dictionary').val(originDict)
  })
});
function validateform(){
    var accusername = document.forms["dictionaryform"]["accusername"].value;
    var dictwords = document.forms["dictionaryform"]["dictionary"].value;
    if (accusername == "" ||  dictwords == "") {
        alert("Please fill out all fields");
        return false;
    }
}