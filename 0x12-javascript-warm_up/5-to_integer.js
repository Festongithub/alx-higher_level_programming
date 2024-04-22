#!/usr/bin/node
const nums = Math.floor(Number(process.argv[2]));
console.log(isNaN(nums) ? 'Not a number':`My number: ${nums}`);
