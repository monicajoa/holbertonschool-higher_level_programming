#!/usr/bin/node
const args = process.argv;
let index;
const number = parseInt(args[2]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (index = 0; index < number; index++) {
    console.log('C is fun');
  }
}
