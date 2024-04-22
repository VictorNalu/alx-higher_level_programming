#!/usr/bin/node

const { argv } = require('process');

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = argv.slice(2);

const x = parseInt(args[0]); // Attempt to convert the first argument to an integer

if (!isNaN(x)) { // Check if the result is not NaN
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
