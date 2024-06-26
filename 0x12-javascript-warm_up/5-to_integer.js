#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = parseInt(args[0], 10);

!isNaN(firstArg) ? console.log(`My number: ${firstArg}`) : console.log('Not a number')
