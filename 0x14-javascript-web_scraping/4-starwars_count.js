#!/usr/bin/node
// script prints the number of movies Wedge Antilles whose character id is 18
// has featured in

let counter = 0;

const req = require('request');
const url = process.argv[2];

req(url, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const allFilms = JSON.parse(body).results;
    for (const i of allFilms) {
      if (i.characters.includes(`https://swapi-api.alx-tools.com/api/people/${18}/`)) {
        counter++;
      }
    }
    console.log(`${counter}`);
  } else {
    console.Error(err);
  }
});
