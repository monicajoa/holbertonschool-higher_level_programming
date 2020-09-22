#!/usr/bin/node
exports.logMe = function (item) {
  this.number = this.number || 0;
  console.log(`${this.number}: ${item}`);
  this.number += 1;
};
