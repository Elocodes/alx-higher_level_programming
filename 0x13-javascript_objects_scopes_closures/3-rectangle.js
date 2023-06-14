#!/usr/bin/node

// print rectangle using the 'x' character
// The repeat function print the character whatever the value of width is
// on same line. THis iterates on new lines till the height of rect is
// exhausted

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
}
module.exports = Rectangle;
