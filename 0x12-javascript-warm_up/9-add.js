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

  // Check if both conversions are successful
  if (!isNaN(num1) && !isNaN(num2)) {
    // Call the add function and print the result
    console.log(add(num1, num2));
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}

