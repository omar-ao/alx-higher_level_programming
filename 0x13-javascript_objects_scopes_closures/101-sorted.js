#!/usr/bin/node

const dict = require('./101-data').dict;
const occurances = new Set(Object.values(dict).sort());
const sorted = {};
let ids = [];
for (const occurance of occurances) {
  ids = [];
  for (const [key, value] of Object.entries(dict)) {
    if (value === occurance) {
      ids.push(key);
    }
  }
  sorted[occurance] = ids;
}
console.log(sorted);
