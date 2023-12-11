#!/usr/bin/node

const numb = process.argv.length;
console.log(numb === 2 ? 'No argument' : numb === 3 ? 'Argument found' : 'Arguments found');
