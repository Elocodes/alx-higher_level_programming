#!/usr/bin/node

// script prints a square using the character X.
// argument. argument must be positive and ocnverted to int.

const args = parseInt(process.argv[2]);
let i;

if (process.argv[2] === 'undefined' || isNaN(args)) console.log('Missing size');
else for (i = 0; i < args; i++) console.log('X'.repeat(args));
