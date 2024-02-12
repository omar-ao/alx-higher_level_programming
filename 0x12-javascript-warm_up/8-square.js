#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log('Missing size');
}

for (let i = 0; i < Number.parseInt(args[2]); i++) {
  for (let i = 0; i < Number.parseInt(args[2]); i++) {
    process.stdout.write('X');
  }
  console.log();
}
