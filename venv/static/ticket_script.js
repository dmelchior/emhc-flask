function calcTime(offset) {
    // create Date object for current location
    var d = new Date();

    // convert to msec
    // subtract local time zone offset
    // get UTC time in msec
    var utc = d.getTime() + (d.getTimezoneOffset() * 60000);

    // create new Date object for different city
    // using supplied offset
    var nd = new Date(utc + (3600000*offset));

    // return time as a string
    return nd.toLocaleString();
}

let today = new Date().toJSON().slice(0, 10);
let time = new Date().toJSON().slice(11,15);
var offsetTime = calcTime(-5);
// document.querySelector("#today").value = today;
document.querySelector("#datetime").value = offsetTime;


