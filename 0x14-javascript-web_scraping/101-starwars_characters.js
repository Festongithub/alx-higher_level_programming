#!/usr/bin/node

const request = require('request');

const endPoint = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(endPoint, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const res = JSON.parse(body).res;
    const list = [];
    res.forEach(res => {
      list.push(new Promise((resolve, reject) => {
        request.get(res, function (err, response, body) {
          if (err) {
            reject(err);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(list).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
