#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});