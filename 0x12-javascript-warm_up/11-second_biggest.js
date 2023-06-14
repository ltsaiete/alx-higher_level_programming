#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length < 2) {
	console.log(0);
} else {
	let second = argv[0];
	let largest = argv[0];

	argv.forEach((n) => {
		if (n > largest) {
			second = largest;
			largest = n;
		} else if (n > second) {
			second = n;
		}
	});
	console.log(second);
}
