#!/usr/bin/node

const fs = require('fs');

const readFile = (filePath) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.log(`An error occurred: ${err.message}`);
    } else {
      console.log(data);
    }
  });
};

const filePath = process.argv[2];

if (!filePath) {
  console.error('Please provide file  path');
  process.exit(1);
}

readFile(filePath);
