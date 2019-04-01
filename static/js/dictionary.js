$(document).ready(function(){
  var originDict = $('#dictionary').val();
  console.log(originDict)
  $('#restart').click(function(){
      $('#dictionary').val(originDict)
  })
});
