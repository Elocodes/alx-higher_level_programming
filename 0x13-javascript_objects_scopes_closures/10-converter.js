#!/usr/bin/node

// function converts a number from base 10 to another base passed as argument.
// An annonymous function is defined using the arrow symbol. it takes
// a parameter 'num' and converts it to the base passed as argument in the
// major function.

exports.converter = function (base) {
  return num => num.toString(base);
};
