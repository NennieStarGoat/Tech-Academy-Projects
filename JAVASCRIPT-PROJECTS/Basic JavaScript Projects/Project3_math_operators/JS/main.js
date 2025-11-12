function Addition_Function() { //Initializes a function that adds two and two and replaces the question in the html document with the answer.
    document.getElementById("Math").innerHTML = "4";
}

function Subtraction_Function() { //Initializes a function that subtracts two from five and concatenates the answer with the question in the html document.
    var Subtraction = 5 - 2;
    document.getElementById("Sub").innerHTML += Subtraction;
}

function Multiplication() { //Initializes a function that multiplies six by eight and replaces the question in the html document with the answer.
    var Easy_Math = 6 * 8;
    document.getElementById("Mult").innerHTML = Easy_Math;
}

function Division() { //Initializes a function that divides forty-eight by six and concatenates the answer with the question in the html document.
    var Simple_Math = 48 / 6;
    document.getElementById("Div").innerHTML += Simple_Math;
}

function More_Math() { //Initializes a function that combines multiple math functions into one and replaces the question in the html document with the answer.
    var Math = (1 + 2) * 3 / 4 - 5;
    document.getElementById("MoMath").innerHTML = Math + " is what 1 + 2, multiplied by 3, divided by 4 and then subtracted by 5 is."
}

function Modulus() { //Initializes a function that does modulus operations and finds the remainder of 25 after dividing by 6 and concatenates the answer with the question in the html document.
    var Mod = 25 % 6;
    document.getElementById("Mod").innerHTML += Mod;
}

function Negation() { //Initializes a function that finds the negative of ten and replaces the question in the html document with the answer.
    var x = 10;
    document.getElementById("Neg").innerHTML = -x;
}

function Increment() { //Initializes a function that increments 5 by 1 and concatenates the answer with the question in the html document.
    var x = 5;
    x++;
    document.getElementById("Inc").innerHTML += x;
}

function Decrement() { //Initializes a function that decrements 5.25 by 1 and replaces the question in the html document with the answer.
    var x = 5.25;
    x--;
    document.getElementById("Dec").innerHTML = x;
}

window.alert(Math.random() * 30); //Creates a popup window displaying a random number between 0 and 30.

function Round() { //Initializes a function that rounds pi and concatenates the answer with the question in the html document.
    var pi = Math.PI;
    document.getElementById("Pi").innerHTML += Math.round(pi);
}