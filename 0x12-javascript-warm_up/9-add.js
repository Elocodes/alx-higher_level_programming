#!/usr/bin/node

// script adds the first 2 numbers passed as argument. numbers must be
// converted to int

const args = process.argv;

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(args[2], args[3]);
