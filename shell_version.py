#!venv/bin/python3
from hangman import Game

game = Game()

print(f'Dica: a palavra tem {game.total_letters} letras e é um(a) {game.tip}')

while True:
    guess = input('Chute: ')
    if game.check_guess(guess):
        game.update()
        print(game)
    else:
        print(f'Erros: {"|" * game.error_count}')

    if game.check_game_over():
        print(f'Você perdeu! a palavra era {game.word}')
        break

    if game.check_game_win():
        print('Parabens! Voce ganhou!')
        break
