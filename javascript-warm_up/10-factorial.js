#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
const myVar = process.argv[2];
if (myVar === undefined) {
  console.log(1);
} else {
  console.log(factorial(myVar));
}
