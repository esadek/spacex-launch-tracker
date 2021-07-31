const countdownElement = document.getElementById('countdown')
const launchDateUnix = countdownElement.dataset.date
const launchDate = new Date(launchDateUnix * 1000)

let countdown = setInterval(function() {
    let currentDate = new Date()
    let difference = launchDate - currentDate
    let days = Math.floor(difference / (1000 * 60 * 60 * 24))
    let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
    let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60))
    let seconds = Math.floor((difference % (1000 * 60)) / 1000)
    countdownElement.innerHTML = days + 'd : ' + hours + 'h : ' + minutes + 'm : ' + seconds + 's'
}, 1000)