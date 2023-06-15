#!/usr/bin/node

// print rectangle using the 'x' character
// The repeat function print the character whatever the value of width is
// on same line. THis iterates on new lines till the height of rect is
// exhausted
// instance method rotate exchanges the values of width and height
// double() multiplies the values of width and height by 2
// square is added as a child class that inherits from rectangle
// function inherits from first square to print the square using the x or c
// characters

const firstSquare = require('./5-square');

module.exports = class Square extends firstSquare {
  charPrint (c = 'X') {
    super.print(c);
    let i;
    if (c !== 'undefined') {
      for (i = 0; i < this.height; i++) console.log(`${c}`.repeat(this.width));
    }
  }
};
