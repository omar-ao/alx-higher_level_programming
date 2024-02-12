#!/usr/bin/node

const args = process.argv;

const lenArgs = args.length - 2;

if (lenArgs === 0) {
  console.log('undefined is undefined');
} else if (lenArgs === 1) {
  console.log(args[2] + ' is ' + 'undefined');
} else {
  console.log(args[2] + ' is ' + args[3]);
}
