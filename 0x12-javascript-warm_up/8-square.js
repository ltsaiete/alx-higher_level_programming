#!/usr/bin/node

const argv = process.argv;
if (argv[2]) {
  if (argv[2] > 0) {
    for (let i = 0; i < argv[2]; i++) {
      console.log('X'.repeat(Number(argv[2])));
    }
  }
} else {
  console.log('Missing size');
}
