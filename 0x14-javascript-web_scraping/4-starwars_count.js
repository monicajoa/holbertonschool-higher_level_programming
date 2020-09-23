#!/usr/bin/node
const request = require('request');
const numberId = '/18/';
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let counter = 0;
  for (const data of JSON.parse(body).results) {
    for (const person of data.characters) {
      if (person.slice(-4) === numberId) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
