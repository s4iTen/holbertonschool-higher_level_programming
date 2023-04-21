#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return 'Rectangle{}';
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
