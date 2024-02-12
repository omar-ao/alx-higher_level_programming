#!/usr/bin/node

const args = process.argv;

const num = args[2];

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number.parseInt(num));
}
