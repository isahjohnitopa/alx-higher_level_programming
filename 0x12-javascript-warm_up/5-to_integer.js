#!/usr/bin/node

let myVar = process.argv[2];
myVar = Math.floor(Number(myVar));
console.log(isNaN(myVar) ? 'Not a number' : `My number is ${myVar}`);
