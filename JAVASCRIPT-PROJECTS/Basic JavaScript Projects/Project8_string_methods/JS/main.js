function Full_Sentence() {
    var part_1 = "I have ";
    var part_2 = "made this ";
    var part_3 = "into a complete ";
    var part_4 = "sentence.";
    var whole_sentence = part_1.concat(part_2, part_3, part_4);
    document.getElementById("Concatenate").innerHTML = whole_sentence;
}

function Slice_Method() {
    var Sentence = "All work and no play makes Johnny a dull boy.";
    var Section = Sentence.slice(27, 33);
    document.getElementById("Slice").innerHTML = Section;
}

function Uppercase() {
    var Sentence = "click here to make me uppercase.";
    result = Sentence.toUpperCase();
    document.getElementById("Upper").innerHTML = result;
}

function Search() {
    text = document.getElementById("Search").innerHTML;
    position = text.search("specific");
    alert(position);
}

function String_Method() {
    var x = 333;
    document.getElementById("Numbers").innerHTML = x.toString();
}

function Precision() {
    var x = 123948.9234570900;
    document.getElementById("Precision").innerHTML = x.toPrecision(7);
}

function Fixed() {
    var num = 59304.34223056;
    document.getElementById("Fixed").innerHTML = num.toFixed(2);
}

function Value() {
    text = "Hello World!";
    document.getElementById("Value").innerHTML = text.valueOf();
}