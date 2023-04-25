#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body).results;
    let count = 0;
    for (const movie in content) {
      const char = content[movie].characters;
      for (const elm in char) {
        if (char[elm].endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
