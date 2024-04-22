#!/usr/bin/node
const { argv } = require('process'); // Changed 'node:process' to 'process'

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log(argv[2]);
}
