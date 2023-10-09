#!/usr/bin/node
// script prints number of tasks completed by userid

const completedTask = {};

const req = require('request');
const url = process.argv[2];

req(url, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const allTasks = JSON.parse(body);
    for (const task of allTasks) {
      if (task.completed) {
        const userId = task.userId;
        if (completedTask[userId]) {
          completedTask[userId]++;
        } else {
          completedTask[userId] = 1;
        }
      }
    }
    console.log(completedTask);
  } else {
    console.Error(err);
  }
});
