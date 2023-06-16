#!/usr/bin/node

// function returns the reversed version of a list

exports.esrever = function (list) {
  const len = list.length;
  const rev = [];
  let i;
  for (i = len - 1; i >= 0; i--) rev.push(list[i]);
  return (rev);
};
