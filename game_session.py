from hangman import Game
from flask import session
import pickle

def get_default_return(game: Game) -> dict:
    return {'total_letters': game.total_letters, 'tip': game.tip,
    'current_game': str(game), 'error_count': game.error_count,
    'is_game_over': game.check_game_over(), 'is_game_won': game.check_game_win()}

def get_game_from_session() -> Game:
    session_game = session.get('game', None)
    if session_game is None: return
    return pickle.loads(session_game)

def store_game_in_session(game: Game) -> None:
    session['game'] = pickle.dumps(game)
    session.modified = True
