#!/usr/bin/node

const argu = process.argv;
console.log(typeof argu[2] === 'undefined' ? 'No Arguments' : argu[2]);
