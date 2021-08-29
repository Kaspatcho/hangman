const wordDiv = document.querySelector('.word')
const guessText = document.querySelector('.guess-text')
const bodyParts = document.querySelectorAll('.pessoa div')
const wrongLetterText = document.querySelector('.wrong-letters')
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

async function startGame() {
    const resp = await fetch(apiUrl, {credentials: 'include', mode: 'cors'})
    const data = await resp.json()
    
    wordDiv.innerText = data.current_game

    document.querySelector('.tip').innerText = `Dica: ${data.tip}`
    alert(`a palavra é um(a) ${data.tip}`)
}

async function sendGuess(guess) {
    try {
        const resp = await fetch(apiUrl + `guess?guess_letter=${guess}`,
        {method: 'POST', credentials: 'include', mode: 'cors'})
        const data = await resp.json()

        wordDiv.innerText = data.current_game

        if (data.error_count > wrongLetterText.innerText.length) {
            if (!wrongLetterText.innerText.includes(guessText.value)) wrongLetterText.innerText += guessText.value
        }

        showBodyParts(data.error_count)
        if(data.is_game_won) alert('VOCE GANHOU!')
        if(data.is_game_over) showGameOverMessage();
    } catch (error) {
        console.error(error)
    }

    guessText.value = ''
}

async function showGameOverMessage() {
    const resp = await fetch(apiUrl + 'gameover',
        {method: 'POST', credentials: 'include', mode: 'cors'})

    const data = await resp.json()
    alert(data.message)
}
