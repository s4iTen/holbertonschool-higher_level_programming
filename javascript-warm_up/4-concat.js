#!/usr/bin/node
const myVar = process.argv[2];
const myVar2 = process.argv[3];
if (myVar === undefined) {
  console.log('undefined is undefined');
} if (myVar !== undefined && myVar2 !== undefined) {
  console.log(myVar + ' is ' + myVar2);
} else if (myVar2 === undefined && myVar !== undefined) {
  console.log(myVar + ' is undefined');
}
