#!/usr/bin/node

const args = process.argv;

const numbers = args.slice(2);
const len = numbers.length;

if (len === 0 || len === 1) {
  console.log(0);
  process.exit(1);
}

console.log(numbers.sort().slice(-2, -1)[0]);
