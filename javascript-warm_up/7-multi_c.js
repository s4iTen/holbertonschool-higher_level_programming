#!/usr/bin/node
const newArgs = process.argv.slice(2);
if (isNaN(newArgs[0]) === false) {
  const n = parseInt(newArgs[0]);
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
