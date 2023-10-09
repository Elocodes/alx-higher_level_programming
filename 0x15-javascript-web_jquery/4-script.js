// JavaScript script that toggles between red and green
// when the user clicks on the tag DIV#toggle_header
// you cant use socument.queryselector
// you must use jquery api

$('DIV#toggle_header').click(function () { 
  $('header').toggleClass('red green');
});
