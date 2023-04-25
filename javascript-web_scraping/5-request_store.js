#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    return;
  }
  fs.writeFile(filepath, body, (err) => {
    if (err) {
      console.error('Error:', err);
    }
  });
});
