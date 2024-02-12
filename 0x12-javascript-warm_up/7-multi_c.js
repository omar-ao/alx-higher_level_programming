#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < Number.parseInt(args[2]); i++) {
  console.log('C is fun');
}
