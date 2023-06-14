#!/usr/bin/node

exports.converter = function (base) {
  return (number) => {
    return number.toString(base);
  };
};
