#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w >= 1 && h >= 1)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
