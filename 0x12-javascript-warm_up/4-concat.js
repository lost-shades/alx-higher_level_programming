#!/usr/bin/node
const args = process.argv.slice(2);

let firstArg;
let secondArg;

if (args[0] !== undefined) {
    firstArg = args[0];
} else {
    firstArg = "undefined";
}

if (args[1] !== undefined) {
    secondArg = args[1];
} else {
    secondArg = "undefined";
}

console.log(firstArg + " is " + secondArg);
