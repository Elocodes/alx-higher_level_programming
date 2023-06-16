#!/usr/bin/node

// script converts first argument to an integer and prints.
// if argument s not given or is not a number, print not a number

const args = parseInt(process.argv[2]);
if (process.argv[2] === 'undefined' || isNaN(args)) console.log('Not a number');
else console.log('My number: ' + args);
