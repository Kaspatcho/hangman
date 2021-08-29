from random import choice
import numpy as np
from typing import Tuple
from word_list import WORDS

ERROR_LIMIT = 5

class Game:
    def __init__(self) -> None:
        self.error_count = 0
        self.tip, self.word = self._get_random_word()
        self.current_game = '_' * len(self.word)
        self.guess = None
        for char in self.word:
            if not char.isalpha(): self._replace_current_game(char)

    def update(self) -> None:
        self._replace_current_game()

    def check_game_win(self) -> bool:
        return self.current_game.lower() == self.word.lower()

    def _replace_current_game(self, replace: str = None) -> None:
        if replace is None: replace = self.guess
        array = np.array(list(self.word.lower()))
        indexes = np.where(array == replace)[0]
        for index in indexes:
            self.current_game = self.current_game[:index] + self.word[index] + self.current_game[index + 1:]

    def __repr__(self) -> str:
        return self.current_game

    def check_guess(self, guess: str) -> bool:
        self.guess = guess.lower().strip()[0]

        is_correct = self.guess in self.word.lower()
        if not is_correct: self.error_count += 1
        return is_correct

    def check_game_over(self) -> bool:
        return self.error_count >= ERROR_LIMIT

    def _get_random_word(self) -> Tuple[str, str]:
        tip = choice(list(WORDS.keys()))
        word = choice(WORDS[tip])
        return tip, word
