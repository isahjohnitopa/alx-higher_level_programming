#!/usr/bin/node

const myVar = Math.floor(Number(process.argv[2]));
console.log(isNaN(myVar) ? 'Not a number' : `My number is ${myVar}`);
