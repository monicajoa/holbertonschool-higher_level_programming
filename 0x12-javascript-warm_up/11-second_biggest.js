#!/usr/bin/node
const args = process.argv;
const newList = [];
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  for (let index = 2; args[index]; index++) {
    newList[index - 2] = parseInt(args[index]);
  }
  newList.sort(function (a, b) {
    return a - b;
  });
  console.log(newList[newList.length - 2]);
}
