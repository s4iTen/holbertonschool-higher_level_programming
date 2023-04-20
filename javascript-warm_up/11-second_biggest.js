#!/usr/bin/node
const Arg = process.argv.slice(2);
if (Arg.length === 0 || Arg.length === 1) {
  console.log(0);
} else {
  Arg.sort((a, b) => a - b);
  console.log(Arg[Arg.length - 2]);
}