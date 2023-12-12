#!/usr/bin/node

const myName = Math.floor(Number(process.argv[2]));
console.log(isNaN(myName) ? 'Not a number' : `My number is ${myName}`);
