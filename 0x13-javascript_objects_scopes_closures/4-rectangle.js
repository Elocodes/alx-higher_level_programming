#!/usr/bin/node

// print rectangle using the 'x' character
// The repeat function print the character whatever the value of width is
// on same line. THis iterates on new lines till the height of rect is
// exhausted
// instance method rotate exchanges the values of width and height
// double() multiplies the values of width and height by 2

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    const a = this.width;
    const b = this.height;
    this.width = b;
    this.height = a;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
