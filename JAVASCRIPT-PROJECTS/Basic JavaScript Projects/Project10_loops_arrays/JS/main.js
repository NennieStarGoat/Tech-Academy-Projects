function Call_Loop() {
    text = "";
    i = 0;
    while (i < 10) {
        text += "<br>The number is " + i;
        i++;
    }
    document.getElementById("Loop").innerHTML = text;
}

function Length() {
    text = "The number is 0 The number is 1 The number is 2 The number is 3 The number is 4 The number is 5 The number is 6 The number is 7 The number is 8 The number is 9";
    length = text.length;
    document.getElementById("Length").innerHTML = length;
}

function For_Loop() {
    var Instruments = ["Guitar", "Drums", "Piano", "Bass", "Violin", "Trumpet", "Flute"];
    var Content = "";
    var Y;
    for (Y = 0; Y < Instruments.length; Y++) {
        Content += Instruments[Y] + "<br>";
    }
    document.getElementById("Instruments").innerHTML = Content;
}

function Cat_Pics() {
    var Cat_Picture = [];
    Cat_Picture[0] = "sleeping";
    Cat_Picture[1] = "playing";
    Cat_Picture[2] = "eating";
    Cat_Picture[3] = "purring";
    document.getElementById("Cat").innerHTML = "In this picture, the cat is " + Cat_Picture[2] + ".";
}

function Pi() {
    let pi = 3.14;
    return pi
}

function Get() {
    document.getElementById("Pi").innerHTML = Pi();
}

let car = {
    make: "Dodge ",
    model: "Viper ",
    year: "2021 ",
    color: "red ",
    description : function() {
        return "The car is a " + this.year + this.color + this.make + this.model;
    }
};
document.getElementById("Car").innerHTML = car.description();