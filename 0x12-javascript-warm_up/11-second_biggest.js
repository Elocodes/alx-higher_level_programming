#!/usr/bin/node

// script prints the second biggest integer in the lis of arguments.
// argument. argument can be ocnverted to int.

if (process.argv.length < 4) {
  console.log('0');
} else {
  const args = process.argv.slice(2);
  args.sort(function (smallest, largest) { return largest - smallest; });
  const secondHighest = args[1];
  console.log(secondHighest);
}
