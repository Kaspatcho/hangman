from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from hangman import Game
from secrets import token_bytes
import pickle

app = Flask(__name__)
app.secret_key = str(token_bytes(16))
CORS(app)

def get_default_return(game: Game) -> dict:
    return {'total_letters': game.total_letters, 'tip': game.tip,
    'current_game': str(game), 'error_count': game.error_count,
    'is_game_over': game.check_game_over(), 'is_game_won': game.check_game_win()}

def get_game() -> Game:
    session_game = session.get('game', None)
    if session_game is None: return session_game
    return pickle.loads(session_game)

def store_game_in_session(game: Game) -> None:
    session['game'] = pickle.dumps(game)

@app.route('/', methods=['GET'])
def root():
    game = Game()
    store_game_in_session(game)
    
    return jsonify(get_default_return(game))


@app.route('/guess', methods=['GET'])
def guess():
    game = get_game()
    if game is None: return 'game not started', 404

    guess_letter = request.args.get('guess_letter', None)

    if guess_letter is None: return 'no guess', 404

    is_correct = game.check_guess(guess_letter)

    if is_correct: game.update()
    
    store_game_in_session(game)

    return get_default_return(game)


app.run(host='localhost', port=5000)
