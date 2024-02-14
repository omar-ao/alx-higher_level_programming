#!/usr/bin/node

const fs = require('node:fs/promises');
const args = process.argv;
const [fileA, fileB, fileC] = args.slice(2);

async function concatFiles () {
  const contentFileA = fileA ? await fs.readFile(fileA) : '';
  const contentFileB = fileB ? await fs.readFile(fileB) : '';

  await fs.appendFile(fileC, contentFileA);
  await fs.appendFile(fileC, contentFileB);
}

concatFiles();
