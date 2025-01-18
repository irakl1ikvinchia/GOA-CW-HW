const myScores = document.getElementById("myScore");
const compScores = document.getElementById("compScore");
const wins = document.getElementById("wins");
const btnsDiv = document.getElementById("btns");
const choices = ["Rock", "Paper", "Scissors"];

let myScore = 0;
let compScore = 0;

btnsDiv.addEventListener("click", function(e) {
    const btnId = e.target.id;
    const compChoice = choices[Math.floor(Math.random() * choices.length)];

    if (btnId === compChoice) {
        wins.textContent = "its a tie";
    } else if ((btnId === "Rock" && compChoice === "Paper") || (btnId === "Scissors" 
        && compChoice === "Rock") || (btnId === "Paper" && compChoice === "Scissors")){
        compScore++;
        compScores.textContent = compScore;
        wins.textContent = "you lost!";
    } else {
        myScore++;
        myScores.textContent = myScore;
        wins.textContent = "you won";
    }
});