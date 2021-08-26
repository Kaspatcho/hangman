from random import choice
import numpy as np
from typing import Tuple

ERROR_LIMIT = 5
WORDS = {
    'país' : [
        'China', 'India', 'Estados Unidos', 'Indonesia', 'Paquistao', 'Brasil', 'Nigeria', 'Bangladesh', 'Russia',
        'Mexico', 'Japao', 'Etiopia', 'Filipinas', 'Egito', 'Vietname', 'Republica Democratica do Congo', 'Turquia',
        'Ira', 'Alemanha', 'Tailandia', 'Reino Unido', 'França', 'Italia', 'Tanzania', 'africa do Sul', 'Myanmar', 'Quenia',
        'Coreia do Sul', 'Colombia', 'Espanha', 'Uganda', 'Argentina', 'Argelia', 'Sudao', 'Ucrania', 'Iraque', 'Afeganistao',
        'Polonia', 'Canada', 'Marrocos', 'Arabia Saudita', 'Uzbequistao', 'Peru', 'Angola', 'Malasia', 'Moçambique', 'Gana',
        'Republica Centro-Africana', 'Nova Zelandia', 'Mauritania', 'Panama', 'Kuwait', 'Croacia', 'Georgia', 'Eritreia',
        'Uruguai', 'Bosnia e Herzegovina', 'Mongolia', 'Armenia', 'Jamaica', 'Catar', 'Albania', 'Porto Rico', 'Lituania',
        'Moldavia', 'Namibia', 'Gambia', 'Botswana', 'Gabao', 'Lesoto', 'Macedonia do Norte', 'Eslovenia', 'Guine-Bissau',
        'Letonia', 'Kosovo', 'Bahrein', 'Guine Equatorial', 'Trinidad e Tobago', 'Estonia', 'Timor-Leste', 'Mauricia', 'Eswatini',
        'Granada', 'Sao Vicente e Granadinas', 'Jersey', 'Aruba', 'Tonga', 'U S  Ilhas Virgens', 'Seicheles', 'Antigua e Barbuda'
    ],
    'nome' : [
        'Djaniny', 'Dinis', 'Alao', 'Cheng', 'Ilie', 'Aaliyah', 'Ibaadali', 'Claudio', 'Hermano', 'Enzu', 'Dailson',
        'Django', 'Arham', 'Johny', 'Cademo', 'Ashan', 'Adja', 'Cooper', 'Ines', 'Havya', 'Aryana', 'Geoffrey',
        'Annalisa', 'Ayana', 'Habacuque', 'Charbel', 'Gislane', 'Djeisen', 'Esenia', 'Estebane', 'Anselmo', 'Asvi',
        'Christopher', 'Amber', 'Halana', 'andria', 'Angeline', 'Harkirat', 'Dario', 'Oswaldo', 'Doralice', 'Dieudonne',
        'Dennys', 'Iryna', 'Dien', 'Harleen', 'Aderito', 'Emmanuela', 'Adla', 'Allister', 'Hercio', 'Cleopatra',
        'Abdulwahab', 'Ennzo', 'Eudes', 'anghel', 'Georgeta', 'Hamda', 'Dhruv', 'Gênesis', 'Esteban', 'Agandeep', 'Gilcelio',
        'Constança', 'Harbin', 'Aihra', 'Bogdan', 'Cizia', 'Bryant', 'Agampreet', 'Christiaan', 'Angelino', 'Jayden', 'Golias',
        'Elona', 'Andersa', 'Greg', 'Alexandru', 'Aksh', 'Helao', 'Elias', 'Ananias', 'Catia', 'Ezairon'
    ],
    'comida' : [
        'Amoras', 'arroz', 'abacate', 'ameixa', 'atum', 'alface', 'Baiao de dois', 'beterraba', 'batata', 'bolo',
        'banana', 'Cuscuz', 'camarao', 'carne', 'cordeiro', 'cereja', 'Damasco', 'dobradinha', 'danone', 'doce de leite',
        'Espaguete', 'empada', 'escondidinho', 'Feijao', 'farofa', 'feijoada', 'framboesa', 'figo', 'Gengibre', 'gorgonzola',
        'groselha', 'goiaba', 'goiabada', 'Iogurte', 'inhame', 'Jabuticaba', 'jaca', 'Kiwi', 'Laranja', 'lasanha', 'limao',
        'Melao', 'melado', 'mel', 'macarrao', 'mostarda', 'maionese', 'manga', 'maca', 'Nozes', 'nachos', 'Ovos', 'omelete',
        'Peixe', 'pepino', 'pimentao', 'pate', 'pimenta', 'Queijo', 'Rosbife', 'rabada', 'rabanada', 'requeijao', 'Sopa',
        'soja', 'Tofu', 'tomate', 'Uvas', 'Vagem'
    ]
}

class Game:
    def __init__(self) -> None:
        self.error_count = 0
        self.tip, self.word = self._get_random_word()
        self.current_game = '_' * len(self.word)
        self.guess = None
        self._replace_current_game(' ')

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
