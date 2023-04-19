#!/usr/bin/node
const myVar = process.argv[2];
if (myVar === undefined) {
  console.log('No argument');
} else { console.log(myVar); }
