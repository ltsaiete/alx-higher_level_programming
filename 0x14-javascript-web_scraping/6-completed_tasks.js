#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { return; }
  const todos = JSON.parse(body);
  const users = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (todo.userId in users) {
        users[todo.userId] = users[todo.userId] + 1;
      } else {
        users[todo.userId] = 1;
      }
    }
  });

  console.log(users);
});
