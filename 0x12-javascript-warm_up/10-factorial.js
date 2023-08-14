#!/usr/bin/node

// Script computes and prints factorial of argument passed in the
// command line. arguments are integers

const args = parseInt(process.argv[2]);

function countdown (n) {
  if (n === 0 || isNaN(args)) return (1);
  return n * countdown(n - 1);
}
console.log(countdown(args));
