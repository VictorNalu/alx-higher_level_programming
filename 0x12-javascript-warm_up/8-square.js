#!/usr/bin/node

const { argv } = require('process');

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = argv.slice(2);

const size = parseInt(args[0]); // Attempt to convert the first argument to an integer

if (!isNaN(size)) { // Check if the result is not NaN
  for (let i = 0; i < size; i++) {
    let row = ''; // Initialize an empty string for each row
    for (let j = 0; j < size; j++) {
      row += 'X'; // Append 'X' to the row string
    }
    console.log(row); // Print the row
  }
} else {
  console.log('Missing size');
}
