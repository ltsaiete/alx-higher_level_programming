#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { return; }
  const movies = JSON.parse(body);

  let countMovies = 0;
  movies.results.forEach(movie => {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) { countMovies++; }
  });
  console.log(countMovies);
});
