#!/usr/bin/node

function addMeMaybe (n, op) {
  op(++n);
}

module.exports = { addMeMaybe };
