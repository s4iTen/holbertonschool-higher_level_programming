#!/usr/bin/node
const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const completedTasksByUser = {};

    data.forEach(function (task) {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error(`Error fetching data: ${error}`);
  }
});
