document.write("Hello World!  "); //Writes Hello World! At the top of an html document.

var A = "This is a string"; //Initializes a variable A with the value "This is a string".

document.write(A); //Writes the above variable.

var B = "This is an initial pop up message string, this time with \'Quotation marks\'."; //Initializes a variable B with the value "This is an initial pop up message string, this time with 'Quotation marks'.".

window.alert(B); //Creates a pop up alert on opening the html document, displaying the above.

var C = "  And now this is another string" + " and another string added. "; //Initializes another variable and concatenates both sets of strings together into one.

document.write(C); //Writes the above variable.

var D = "This is D. ", E = "This is E. ", F = "This is F. "; //Initializes multiple variables within the same block of code, any of them may be called.

document.write(F); //Writes the above variable F specifically.

document.write(3 * 3); //Writes the result of the mathematical operation, 9.

function My_First_Function() { //Initializes a function that turns a button's text once clicked on within the html document.
    var str = "This is the button text!";
    document.getElementById("Button_Text").innerHTML = str;
}

var Sent1 = "This is the beginning of the string", Sent2 = " and this is the end of the string."; //Initializes two variables within the same block of code to be called and concatenated below.

document.write(Sent1 + Sent2);