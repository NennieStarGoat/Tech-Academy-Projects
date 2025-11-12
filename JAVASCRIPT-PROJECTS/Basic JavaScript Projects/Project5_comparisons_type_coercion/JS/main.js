document.write(typeof 5);
document.write(" 10" + 5 + " ");
document.write(-2E310 + " ");
document.write(2E310 + " ");
document.write(10 > 2);
document.write(" ");
document.write(2 > 10);
document.write(" ");
document.write(3 == 3);
document.write(" ");
document.write(3 == 13);

function Test() {
    document.getElementById("Test").innerHTML = 0/0;
    document.getElementById("Test1").innerHTML = isNaN('This is a string');
    document.getElementById("Test2").innerHTML = isNaN('007');
}

console.log(2 + 2);
console.log(2 > 10);

x = 10;
y = 10;
z = "11";
a = 11;
b = 3;
document.write(" ");
document.write(x === y);
document.write(" ");
document.write(y === z);
document.write(" ");
document.write(z === a);
document.write(" ");
document.write(a === b);
document.write(" ");
document.write(5 > 2 && 10 > 4);
document.write(" ");
document.write(5 > 10 && 10 > 4);
document.write(" ");
document.write(5 > 10 || 10 > 4);
document.write(" ");
document.write(5 > 10 || 10 > 20);

function Not_Function() {
    document.getElementById("Not").innerHTML = !(20 > 10);
    document.getElementById("Not1").innerHTML = !(5 > 10);
}