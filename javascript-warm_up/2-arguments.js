#!/usr/bin/node
const myVar = process.argv[2];

if (process.argv[3]) {
  console.log('Arguments found');
} else if (myVar === undefined) {
  console.log('No argument');
} else { console.log('Argument found'); }
