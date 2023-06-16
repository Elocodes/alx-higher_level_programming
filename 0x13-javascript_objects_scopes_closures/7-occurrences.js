#!/usr/bin/node

// function returns the number of ocurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let i;
  let counter = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) counter += 1;
  }
  return (counter);
};
