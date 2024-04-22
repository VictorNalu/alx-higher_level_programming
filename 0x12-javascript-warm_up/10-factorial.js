#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  } else if (isNaN(n)) { // Factorial of NaN is 1
    return 1;
  } else {
    // Recursive case: n * factorial(n-1)
    return n * factorial(n - 1);
  }
}

// Extract the command-line argument and convert it to an integer
const num = parseInt(process.argv[2]);

// Print the factorial of the integer
console.log(factorial(num));
