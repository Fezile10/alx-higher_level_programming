#!/usr/bin/node
// Get the number of arguments passed to the script
const numArgs = process.argv.length - 2;

// Use console.log to print the message
if (numArgs === 0) {
  console.log("No argument");
} else if (numArgs === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
