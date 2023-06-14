#!/usr/bin/node

const argvLength = process.argv.length;

if (argvLength === 2) {
  console.log('No argument');
} else if (argvLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
