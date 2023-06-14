#!/usr/bin/node

// script prints a message based on the number of arguments passed
// in the command line

// importing the process module
const process = require('process');

const args = process.argv;
let counter = -1;

args.forEach((argment) => {
  counter += 1;
});

if (counter < 2) console.log('No argument');
if (counter === 2) console.log('Argument found');
if (counter > 2) console.log('Arguments found');
