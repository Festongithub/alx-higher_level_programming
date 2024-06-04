#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
    const json = JSON.parse(body);
    const charFilms = json.result.filter(y => y.characters.find(x => x.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
