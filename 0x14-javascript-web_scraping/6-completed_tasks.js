#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const completedTask = {};
  for (const task of data) {
    if (task.completed === true) {
      if (task.userId in completedTask) {
        completedTask[task.userId] += 1;
      } else {
        completedTask[task.userId] = 1;
      }
    }
  }
  console.log(completedTask);
});
