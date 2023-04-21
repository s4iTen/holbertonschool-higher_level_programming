#!/usr/bin/node

exports.converter = function (base) {
  function recursiveConverter (number) {
    if (number < base) {
      return number.toString();
    } else {
      return recursiveConverter(Math.floor(number / base)) + (number % base).toString();
    }
  }
  return recursiveConverter;
};
