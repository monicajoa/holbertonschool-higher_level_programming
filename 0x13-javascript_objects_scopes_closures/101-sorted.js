#!/usr/bin/node
const dict = require('./101-data').dict;
const dictNew = {};
for (const [key, value] of Object.entries(dict)) {
  if (dictNew[value] === undefined) {
    dictNew[value] = [key];
  } else {
    dictNew[value].push(key);
  }
}
console.log(dictNew);
