#!/usr/bin/node
const Arg = process.argv.length - 2;
if (Arg <= 2) {
  console.log(0);
} else {
  console.log(Arg - 2);
}
