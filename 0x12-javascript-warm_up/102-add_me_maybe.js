#!/usr/bin/noode
exports.addMayBe = function (number, theFunction) {
	theFunction(++number);
};
