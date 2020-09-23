#!/usr/bin/node
const request = require('request');
const requestUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(requestUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movieChars = JSON.parse(body).characters;
  for (const character of movieChars) {
    request(character, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
