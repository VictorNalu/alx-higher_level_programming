#!/usr/bin/node

const { argv } = require('process');

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = argv.slice(2);

const num = parseInt(args[0]); // Attempt to convert the first argument to an integer

if (!isNaN(num)) { // Check if the result is not NaN
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
