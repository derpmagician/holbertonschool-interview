#!/usr/bin/node
const request = require('request');
const id = process.argv[2]

function filmRequest (url) {
  request(url, async function (error, response, body) {
    for (const charURL of JSON.parse(body).characters) {
      if (error) {
        console.log(`Error: ${error}`);
        return;
      }
      const charJSON = await requestChar(charURL);
      console.log(JSON.parse(charJSON).name);
    }
  });
}

function requestChar (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) reject(error);
      else resolve(body);
    });
  });
}

filmRequest(`https://swapi-api.hbtn.io/api/films/${id}/`);