#!/usr/bin/node
// script displays the status code of a get request

const req = require('request');
req(process.argv[2], (err, res) => {
  if (err) throw err;
  console.log('code:', res.statusCode);
});
