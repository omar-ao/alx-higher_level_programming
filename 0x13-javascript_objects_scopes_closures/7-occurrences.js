#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurances = 0;
  for (const element of list) {
    if (element === searchElement) {
      occurances++;
    }
  }
  return occurances;
};
