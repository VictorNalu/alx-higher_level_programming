#!/usr/bin/node

const { argv } = require('process');

// Extract command-line arguments excluding the first two (which are node and the script file)
const args = argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
