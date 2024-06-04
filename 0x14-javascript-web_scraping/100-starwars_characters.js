#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }

  try {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    charactersUrls.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error('Status:', charResponse.statusCode);
          return;
        }

        const character = JSON.parse(charBody);
        console.log(character.name);
      });
    });
  } catch (parseError) {
    console.error('Parse Error:', parseError);
  }
});
