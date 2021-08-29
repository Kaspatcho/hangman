const wordDiv = document.querySelector('.word')
const guessText = document.querySelector('.guess-text')
const bodyParts = document.querySelectorAll('.pessoa div')
const apiUrl = 'http://localhost:5000/'

startGame()

guessText.addEventListener('keyup', e => {
    if(e.keyCode == 13) { // 13 = ENTER
        sendGuess(e.target.value)
    }
})

function showBodyParts(count) {
    for(let i=0; i < Math.min(count, bodyParts.length); i++) {
        bodyParts[i].classList.remove('hidden')
    }
}

async function sendGuess(guess) {
    try {
        const resp = await fetch(apiUrl + `guess?guess_letter=${guess}`,
        {credentials: 'include', method: 'POST'})
        const data = await resp.json()

        wordDiv.innerText = data.current_game
        showBodyParts(data.error_count)
    } catch (error) {
        console.error(error)
    }

    guessText.value = ''
}

async function startGame() {
    const resp = await fetch(apiUrl, {credentials: 'include'})
    const data = await resp.json()
    
    wordDiv.innerText = data.current_game
    alert(`a palavra é um(a) ${data.tip}`)
}
