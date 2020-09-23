#!/usr/bin/node
const request = require('request');
const requestUrl = process.argv[2];
request(requestUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    const toObj = JSON.parse(body);
    for (let i = 0; toObj.results[i]; i++) {
      for (let j = 0; toObj.results[i].characters[j]; j++) {
        if (
          toObj.results[i].characters[j] ===
          'https://swapi-api.hbtn.io/api/people/18/'
        ) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
