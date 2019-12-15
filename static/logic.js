let status1 = document.getElementById("status1");
let status2 = document.getElementById("status2");
let status3 = document.getElementById("status3");

let allButtonOn = document.getElementById("allButtonOn");
let allButtonOff = document.getElementById("allButtonOff");

let button1 = document.getElementById("button1");
let button2 = document.getElementById("button2");
let button3 = document.getElementById("button3");


let statusLampsHTML = [status1, status2, status3];
let buttonLamps = [button1, button2, button3];


function startup() {
    allButtonOff.innerHTML = 'Turn Off All'
    allButtonOff.style.backgroundColor = 'rgba(54, 58, 50, 0.596)'
    allButtonOff.style.color = 'rgb(199, 184, 184)'

    allButtonOn.innerHTML = 'Turn On All'
    allButtonOn.style.backgroundColor = 'rgb(250, 184, 2)'
    allButtonOn.style.color = 'rgb(0, 0, 0)'

}


const adjustBrightness = (brightness) => {
    if (brightness < 20) color = 'rgb(163, 145, 10)'
    else if (brightness < 40 && brightness > 21) color = 'rgb(196, 173, 2)'
    else if (brightness < 60 && brightness > 41) color = 'rgb(222, 214, 0)'
    else if (brightness < 80 && brightness > 61) color = 'rgb(235, 226, 7)'
    else color = 'rgb(255, 255, 0)'

    return color
}

const onclickLamps = (led, brightness) => {
    if (buttonLamps[led].innerText === 'Turn On') {
        turnOff(led)
        statusLampsHTML[led].style.backgroundColor = adjustBrightness(brightness)
    } else {
        turnOn(led, brightness)
        statusLampsHTML[led].style.backgroundColor = 'rgb(49, 47, 47)'
    }
}


const turnOn = (led, brightness) => {
    buttonLamps[led].style.backgroundColor = adjustBrightness(brightness)
    buttonLamps[led].innerText = 'Turn On'
    buttonLamps[led].style.color = 'rgb(0, 0, 0)'
}

const turnOff = (led) => {
    buttonLamps[led].style.backgroundColor = 'rgba(54, 58, 50, 0.596)'
    buttonLamps[led].innerText = 'Turn Off'
    buttonLamps[led].style.color = 'rgb(199, 184, 184)'
}

const onclickAllLamps = (status, brightness) => {
    if (status === "ToTurnOn") {
        for (let i = 0; i < 3; i++) {

            turnOff(i)
            statusLampsHTML[i].style.backgroundColor = adjustBrightness(brightness)

        }
    } else {
        for (let i = 0; i < 3; i++) {
            turnOn(i, brightness)
            statusLampsHTML[i].style.backgroundColor = 'rgb(49, 47, 47)'
        }
    }
}

startup()