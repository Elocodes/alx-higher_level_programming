#!/usr/bin/node

// function prints argument passed to it and its number

let counter = 0;

exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
