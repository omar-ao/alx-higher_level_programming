#!/usr/bin/node

const args = process.argv;

const numbers = args.slice(2);

if (numbers.length === 0) {
  console.log(0);
  process.exit(1);
}

if (numbers.length === 1) {
  console.log(1);
  process.exit(1);
}

let max = numbers[0];
for (const num of numbers) {
  if (max < num) {
    max = num;
  }
}

console.log(max);
process.exit(1);
