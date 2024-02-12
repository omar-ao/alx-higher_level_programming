#!/usr/bin/node

const args = process.argv;
const num = args[2];

if (!num || isNaN(num)) {
  console.log('Missing size');
}

let line = '';
for (let i = 0; i < Number.parseInt(args[2]); i++) {
  line = '';
  for (let i = 0; i < Number.parseInt(args[2]); i++) {
    line += 'X';
  }
  console.log(line);
}
