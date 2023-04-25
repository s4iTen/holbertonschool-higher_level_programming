#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const tasks = JSON.parse(body);
  const completedTasksByUser = {};
  tasks.forEach(function (task) {
    if (task.completed) {
      if (!completedTasksByUser.hasOwnProperty(task.userId)) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId]++;
    }
  });
  console.log(completedTasksByUser);
});
