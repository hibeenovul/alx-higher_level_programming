#!/usr/bin/node

let biggest = 0;
let a
const arrayNumbers = [];

for (a = 2; a < process.argv.length; a++) {
  if (Number.isNaN(parseInt(process.argv[a])) === false) {
    arrayNumbers[a - 2] = parseInt(process.argv[a]);
  }
}

if (arrayNumbers.length > 1) {
  biggest = Math.max.apply(null, arrayNumbers);
  a = arrayNumbers.indexOf(biggest);
  arrayNumbers[a] = -Infinity;
  biggest = Math.max.apply(null, arrayNumbers);
}

console.log(biggest);
