#!/usr/bin/node
// script gets the contenet of a webpage and store it in a file

const req = require('request');
const url = process.argv[2];
const storageF = process.argv[3];
const fs = require('fs');

req(url, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    fs.writeFile(storageF, body, 'utf8', (err) => {
      if (err) throw err;
    });
  } else {
    console.Error(err);
  }
});
