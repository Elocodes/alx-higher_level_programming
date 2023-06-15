#!/usr/bin/node

// print rectangle using the 'x' character
// The repeat function print the character whatever the value of width is
// on same line. THis iterates on new lines till the height of rect is
// exhausted
// instance method rotate exchanges the values of width and height
// double() multiplies the values of width and height by 2
// square is added as a child class that inherits from rectangle

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super (size, size);
  }
}
