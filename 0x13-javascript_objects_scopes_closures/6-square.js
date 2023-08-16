#!/usr/bin/node

// The Square class here inherits from the square class of task 5.
// in this task, we create an instance method "charPrint(c) that prints
// the rectangle using the character c.
// if c is undefined, use the character x.

const InitialSquare = require('./5-square');

module.exports = class Square extends InitialSquare {
  charPrint (c) {
    let i;
    if (c === undefined) super.print();
    else for (i = 0; i < this.height; i++) console.log(`${c}`.repeat(this.width));
  }
};
