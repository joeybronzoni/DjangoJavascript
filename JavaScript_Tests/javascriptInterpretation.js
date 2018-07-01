// JS-Interpretation:
/* .filter
   -Describe what this function does and Identify an alternative method
    using vanilla JS
*/


$("input:hidden").filter(function() {
  if ($(this).val() == "") {
	$(this).val(-1);
  }
});

/* So this function is grabbing all of the input elements with the type=hidden. This might be used to
   send information back to a server when A form is submitted using other attributes. I believe this
   has to do with the statelessness of HTTP1 even though inpractice and requests are not really associated with
   each other except for some shared info that the server can know about, i.e.-like the value from a hidden attribute.
*/

/*
   A way to fullfill the same thing in vanilla javascript (I know some people don't like referring to it like this but I like vanilla and you mentioned coldstone so...)
   would be like grabbiing all the inputs in a number of ways and iterating through them to change the value
*/


var elements = document.querySelectorAll('input[type="hidden"]');
// now we have all the inputs with the value=""
for (let i = 0, input; input = elements[i++];) {
  if (input.value === "")
	input.value = -1;
  console.log(`value is now -1 for ${input}`);
};
