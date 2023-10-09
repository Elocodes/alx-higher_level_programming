// JavaScript script that updates the text color of a <header> element
// to red (#FF0000) when the user clicks on the tag DIV#red_header
// you cant use socument.queryselector
// you must use jquery api

$('DIV#red_header').click(function () { 
  $('header').css('color', '#FF0000');
});
