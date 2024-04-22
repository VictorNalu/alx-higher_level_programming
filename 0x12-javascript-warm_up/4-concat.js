#!/usr/bin/node
const { argv } = require('process'); // Changed 'node:process' to 'process'

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = argv.slice(2);

if (args.length === 0) {
  console.log('undefined is undefined');
} else if (args.length === 1) {
  console.log(args[0], 'is undefined');
} else if (args.length === 2) {
  console.log(args[0], 'is', args[1]);
}
