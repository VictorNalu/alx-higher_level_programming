#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = process.argv.slice(2);

// Check if both arguments are provided
if (args.length === 2) {
  // Convert arguments to integers
  const num1 = parseInt(args[0]);
  const num2 = parseInt(args[1]);
  const m = add(num1, num2);
  console.log(m);
} else {
  console.log('NaN');
}
