function getDate(){
    var d=new Date();
    var fmt=d.toLocaleDateString();
    document.getElementById("date").innerHTML=fmt;
}

function rotateImg(){
    document.getElementById("i1").style.transform="rotate(360deg)";
    document.getElementById("i1").style.transitionDuration="7s";
}
