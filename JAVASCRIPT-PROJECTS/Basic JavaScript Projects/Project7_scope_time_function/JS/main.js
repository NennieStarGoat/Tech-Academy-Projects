function Add_Numbers_1() {
    var X = 10;
    document.write(20 + X + "<br>");
    console.log(15 + X);
}

function Add_Numbers_2() {
    document.write(X + 100);
    console.log(X + 100);
}

Add_Numbers_1();
Add_Numbers_2();

function Get_Date() {
    if (new Date().getHours() < 18) {
        document.getElementById("Greeting").innerHTML = "How are you today?";
    }
}

function Get_Omen() {
    if (new Date().getMonth() == 5) {
        document.getElementById("Omen").innerHTML = "The trees are watching, and are scared.";
    }
}

function Age_Function() {
    Age = document.getElementById("Age").value;
    if (Age >= 18) {
        Vote = "You are old enough to vote!";
    }
    else {
        Vote = "You are not old enough to vote!";
    }
    document.getElementById("How_Old").innerHTML = Vote;
}

function Time_Function() {
    var Time = new Date().getHours();
    var Reply;
    if (Time < 12 == Time > 0) {
        Reply = "It is morning time!";
    }
    else if (Time >= 12 == Time < 18) {
        Reply = "It is afternoon.";
    }
    else {
        Reply = "It is evening time.";
    }
    document.getElementById("Day_Time").innerHTML = Reply;
}