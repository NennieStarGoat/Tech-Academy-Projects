function My_First_Function() {
	var String = "You pet the goat! <p><b>Congratulations!</b> <p>The goat, <i>Imogen</i>, is <u>very happy</u>.";
	var result = String.fontcolor("green");
	document.getElementById("Goat").innerHTML =
	result;
}