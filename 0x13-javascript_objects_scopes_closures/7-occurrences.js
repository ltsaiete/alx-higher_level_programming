#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;

  list.forEach((element) => {
    if (element === searchElement) n++;
  });
  return n;
};
