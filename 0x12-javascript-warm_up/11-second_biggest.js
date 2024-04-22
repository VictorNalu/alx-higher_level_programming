#!/usr/bin/node

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = process.argv.slice(2);

// Check if there are no arguments or only one argument
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers and remove duplicates
  const numbers = args.map(Number).filter((num, index, self) => !isNaN(num) && self.indexOf(num) === index);

  // Sort the numbers in descending order
  numbers.sort((a, b) => b - a);

  // Print the second biggest integer if it exists
  if (numbers[1] !== undefined) {
    console.log(numbers[1]);
  } else {
    console.log(0);
  }
}
