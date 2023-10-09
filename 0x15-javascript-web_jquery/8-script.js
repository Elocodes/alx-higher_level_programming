// JavaScript script that fetches the title for all movies from a URL
// All movie titles must be list in the HTML tag UL#list_movies
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (body) {
  const allMovies = JSON.parse(body).results;
  allMovies.forEach(movie => $('UL#list_movies').append(`<li>${movie.title}</li>`));
});
