const canvas = document.getElementById('drawing-board');
const toolbar = document.getElementById('toolbar');
const guessButton = document.getElementById('guess')
const predictionString = document.getElementById('guess_header')
const ctx = canvas.getContext('2d');

canvas.width = 1000;
canvas.height = 1000;

ctx.fillStyle = "#FFFFFF";
ctx.fillRect(0, 0, canvas.width, canvas.height);
canvas.style.backgroundColor="white";
canvas.style.color="black";

let isPainting = false;
let lineWidth = 3;
let out;
let guessed = false;

const draw = (e) => {
    if(!isPainting) {
        return;
    }

    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';

    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
}

canvas.addEventListener('mousedown', (e) => {
    isPainting = true;
});

canvas.addEventListener('mouseup', e => {
    isPainting = false;
    ctx.stroke();
    ctx.beginPath();
});

canvas.addEventListener('mousemove', draw);

canvas.addEventListener('mouseleave', e => {
    isPainting = false;
    ctx.stroke();
    ctx.beginPath();
});

window.addEventListener('scroll', e => {
    isPainting = false;
    ctx.stroke();
    ctx.beginPath();
})

function guesser(){
    if (guessed==false){
        predictionString.textContent="A.I. Guess: LOADING..." ;
        predict();
        guessButton.style.backgroundColor = "#bfbfbf";
        guessButton.style.color = "grey";
        guessed = true;
    }
    else{
        console.log("Already Guessed... Reset before continuing...");
    }
}

function predict() {
    var dataURL = canvas.toDataURL("image/png");
    $.ajax({
        type: "POST",
        url: "/postmethod",
        contentType: "application/json",
        data: JSON.stringify({out: dataURL}),
        dataType: "json",
        success: function(response) {
            console.log(response.guess);
            out = String(response.guess);
            predictionString.textContent="A.I. Guess: " + out ;
            return response
        },
        error: function(err) {
            console.log(err);
            out = "Failed to Guess";
            predictionString.textContent="A.I. Guess: " + out ;
            return err
        }
    });
}

function resetCanvas(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    console.log("Cleared")
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    predictionString.textContent="A.I. Guess:";
    guessed = false;
    guessButton.style.backgroundColor = "grey";
    guessButton.style.color = "white";
}