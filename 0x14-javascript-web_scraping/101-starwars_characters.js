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
    const charactersPromises = [];

    charactersUrls.forEach(characterUrl => {
      charactersPromises.push(new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
            return;
          }

          if (charResponse.statusCode !== 200) {
            reject(new Error(`Status: ${charResponse.statusCode}`));
            return;
          }

          const character = JSON.parse(charBody);
          resolve(character.name);
        });
      }));
    });

    Promise.all(charactersPromises)
      .then(characters => {
        characters.forEach(characterName => {
          console.log(characterName);
        });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } catch (parseError) {
    console.error('Parse Error:', parseError);
  }
});
