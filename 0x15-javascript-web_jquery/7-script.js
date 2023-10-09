// JavaScript script that fetches the character name from a URL
// The name must be displayed in the HTML tag DIV#character
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (res) {
  $('DIV#character').text(res.name);
});
