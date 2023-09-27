#!/usr/bin/node
// script prints the title of a star war moview  where the
// episode num matches integer passed as arg

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
