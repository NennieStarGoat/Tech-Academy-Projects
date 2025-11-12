function My_Dictionary(){
    var Doggos = {
        small: "Chihuahua",
        medium: "Australian Cattle Dog",
        large: "German Shepard",
        extralarge: "Great Dane",
        humongous: "English Mastiff"
    };
    delete Doggos.small;
    document.getElementById("Dictionary").innerHTML = Doggos.small;
}