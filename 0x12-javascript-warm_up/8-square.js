#!/usr/bin/node
const args = process.argv;
let index;
const number = parseInt(args[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (index = 0; index < number; index++) {
    console.log('X'.repeat(number));
  }
}
