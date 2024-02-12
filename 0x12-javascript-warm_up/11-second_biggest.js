#!/usr/bin/node

const args = process.argv;

const numbers = args.slice(2);
const len = numbers.length;

if (len > 1) {
  numbers.sort(function(a, b) {
    return a - b;
  });
  console.log(numbers.slice(-2, -1)[0]);
} else {
  console.log(0);
}
