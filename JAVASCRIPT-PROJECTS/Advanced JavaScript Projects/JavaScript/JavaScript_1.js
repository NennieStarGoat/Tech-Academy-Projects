function Flower_Function() {
    var Flower_Output;
    var Flowers = document.getElementById("Flower_Input").value;
    var Flower_String = " are beautiful flowers!";
    switch (Flowers) {
        case "Black Eyed Susans":
            Flower_Output = "Black Eyed Susans" + Flower_String;
            break;
        case "Sunflowers":
            Flower_Output = "Sunflowers" + Flower_String;
            break;
        case "Columbines":
            Flower_Output = "Columbines" + Flower_String;
            break;
        case "Roses":
            Flower_Output = "Roses" + Flower_String;
            break;
        case "Carnations":
            Flower_Output = "Carnations" + Flower_String;
            break;
        case "Irises":
            Flower_Output = "Irises" + Flower_String;
            break;
        default:
            Flower_Output = "Please enter a flower exactly as written on the above list.";
    }
    document.getElementById("Output").innerHTML = Flower_Output;
}

function Hello_World_Function() {
    var A = document.getElementsByClassName("Click");
    A[0].innerHTML = "The text has changed!";
}

var c = document.getElementById("Circle");
var ctx = c.getContext("2d");
ctx.beginPath();
ctx.arc(95, 50, 40, 0, 2*Math.PI);
ctx.stroke();

const grd = ctx.createLinearGradient(180, 100, 270, 0);
grd.addColorStop(0, "green");
grd.addColorStop(1, "blue");

ctx.fillStyle = grd;
ctx.fillRect(200, 20, 170, 100);