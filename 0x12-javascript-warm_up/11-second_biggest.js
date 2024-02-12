#!/usr/bin/node

const arr = process.argv;

const args = arr.slice(2);
const len = args.length;

if (len > 1) {
  const numbers = args.map(function (n) {
    return parseInt(n);
  });
  console.log(numbers.sort().slice(-2, -1)[0]);
} else {
  console.log(0);
}
