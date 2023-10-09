// JavaScript script that adds the class red to a <header> element
// when the user clicks on the tag DIV#red_header
// you cant use socument.queryselector
// you must use jquery api

$('DIV#red_header').click(function () { 
  $('header').addClass('red');
});
