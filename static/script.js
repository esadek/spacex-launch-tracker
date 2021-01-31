const countdownElement = document.getElementById("countdown")
const launchDateUnix = countdownElement.dataset.date
const launchDate = new Date(launchDateUnix * 1000)

var countdown = setInterval(function() {
    var currentDate = new Date()
    var difference = launchDate - currentDate
    var days = Math.floor(difference / (1000 * 60 * 60 * 24))
    var hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
    var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60))
    var seconds = Math.floor((difference % (1000 * 60)) / 1000)
    countdownElement.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s"
}, 1000)