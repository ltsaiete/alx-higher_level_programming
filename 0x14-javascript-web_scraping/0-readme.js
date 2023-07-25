#!/usr/bin/node
const fs = require('fs');

const args = process.argv;

fs.readFile(args[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});
