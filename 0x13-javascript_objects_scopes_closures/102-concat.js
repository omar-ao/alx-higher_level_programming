#!/usr/bin/node

const fs = require('node:fs/promises');

async function concatFiles () {
  try {
    const fileA = await fs.readFile('fileA',
      { encoding: 'utf8' });
    const fileB = await fs.readFile('fileB',
      { encoding: 'utf8' });

    await fs.appendFile('fileC', fileA);
    await fs.appendFile('fileC', fileB);
  } catch (err) {
    console.log(err);
  }
}

concatFiles();
