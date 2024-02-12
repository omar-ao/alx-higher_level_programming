#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('NaN');
}

const first = Number.parseInt(args[2]);
const second = Number.parseInt(args[3]);

console.log(first + second);
