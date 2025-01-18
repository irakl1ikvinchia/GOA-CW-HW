const box = document.getElementById("div2");

let position = 0;
let direction = 1;

function animateBox() {
    position += direction;

    if (position >= 400){
        direction = -1;
    } else if (position <= 0){
        direction = 1;
    }

    box.style.left = position + "px";
}

setInterval(animateBox, 20);