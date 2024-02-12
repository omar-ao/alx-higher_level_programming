#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  console.log(a + b);
  return 0;
}

const first = Number.parseInt(args[2]);
const second = Number.parseInt(args[3]);

add(first, second);
