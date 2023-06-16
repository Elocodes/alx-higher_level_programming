#!/usr/bin/node

// script prints a statement 'c is fun' the number of times passed in
// argument. argument must be positive and ocnverted to int.

const args = parseInt(process.argv[2]);
let i;

if (process.argv[2] === 'undefined' || isNaN(args)) console.log('Missing number of occurrences');
else for (i = 0; i < args; i++) console.log('C is fun');
