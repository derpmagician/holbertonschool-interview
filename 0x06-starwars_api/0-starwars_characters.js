#!/usr/bin/node
const request = require('request');
const id = process.argv[2]
const url = `https://swapi-api.hbtn.io/api/films/${id}/?format=json`;
request.get(url, function (response, body) {
  const film = (JSON.parse(body.body));
  character(film.characters);
});
const character = (people, i = 0) => {
  if (i === people.length) return;
  request.get(people[i], function (response, body) {
    console.log(JSON.parse(body.body).name);
    character(people, i + 1);
  });
};
