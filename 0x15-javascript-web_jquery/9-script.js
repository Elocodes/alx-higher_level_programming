// JavaScript script that fetches from a URL
// and displays the value of hello in the HTML tag DIV#hello
// Your script must work when it is imported from the <head> tag
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API

$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (body) {
    $('DIV#hello').text(body.hello);
  });
});
