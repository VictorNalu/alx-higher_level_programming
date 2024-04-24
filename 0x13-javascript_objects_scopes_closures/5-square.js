#!/usr/bin/node
// Importing the Rectangle class from '4-rectangle' file
const Rectangle = require('./4-rectangle');

// Defining the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Calling the parent class constructor
    super(size, size);
  }
}

// Exporting the Square class
module.exports = Square;
