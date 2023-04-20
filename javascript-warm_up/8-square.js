#!/usr/bin/node
const newArgs = process.argv.slice(2);
if (isNaN(newArgs[0]) === false) {
  const n = parseInt(newArgs[0]);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
