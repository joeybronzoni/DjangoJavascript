
// Palindrome:
/* Flags
   -Case sensitive: C
   -Spaces removed: S
   -Puncuation removed: P
   -Not a palindrome: F
*/


// TODO:
/* List
   -create simple html page that takes input from user and displays
   the different type of strings for palindromes
*/


// create function that tests for a palindrom and return a value for each instance:
function testPali(str) {

  let flags = [];
  regex =/s/;

  var lcStr = str.toLowerCase(str);

  // test for spaces in given string
  var inValid = /\s/;
  var test = inValid.test(str);

  // if spaces are found push the letter S to the flags array
  if (test) {
  	console.log('S');
	flags.push('S');
	console.log(flags ,'flags = S');
  } else {
  	console.log('no spaces found');
  }


  // test for different case of a string, if mixed case is found add 'C' to the array
  var my =/[a-z][A-Z]/.test(str);
  if (my === true) {
	console.log('C');
	flags.push('C');
	console.log('flags: ', flags);
  }

  // create function that tests that string is a palindrome and return Boolean
  function checkPali(str) {
	var re = /[^A-Za-z0-9]/g;
	str = str.toLowerCase().replace(re, "");

	var len = str.length;
	for (let i = 0; i < len/2; i++) {
	  if (str[i] !== str[len -1 - i]) {
		return false;
	  }
	}
	return true;

  }
  // Get value of palindrome function, if(true) push to the flag array
  if (checkPali(str) === true) {
	flags.push('T');
	console.log(flags);

  }

}

// just some test cases to try
string1 = 'RISE TOVOTE SIR';
string2 = 'rise tovote sir';
string3 = 'rISE tOVOTe SIR';
string3 = 'madam';
//testPali(string1);
//testPali(string2);
testPali(string3);
