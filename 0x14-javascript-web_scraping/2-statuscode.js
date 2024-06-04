#!/usr/bin/node

const request = require('request');
const process = require('process');

// get the url
const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    console.log(`code: ${response.statusCode}`);
  }
});
