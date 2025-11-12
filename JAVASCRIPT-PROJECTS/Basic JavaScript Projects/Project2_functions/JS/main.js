function Second_Function() { //Initializes a function that turns a button's text once clicked on within the html document.
    var str = "This is the button text!", str2 = " You've done it!";
    document.getElementById("Button_Text").innerHTML = str + str2;

    document.getElementById("Paragraph").innerHTML += " But surprise! There is more!"; //Concatenates and adds onto the Paragraph element in the html document.
}