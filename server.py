
# {
#     "current_game": string,
#     "error_count": int,
#     "is_game_over": boolean,
#     "is_game_won": boolean,
#     "tip": string,
#     "total_letters": int
# }


from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from flask_session import Session
from hangman import Game
from secrets import token_bytes
import pickle

app = Flask(__name__)
app.secret_key = str(token_bytes(16))
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)
CORS(app)

def get_default_return(game: Game) -> dict:
    return {'total_letters': game.total_letters, 'tip': game.tip,
    'current_game': str(game), 'error_count': game.error_count,
    'is_game_over': game.check_game_over(), 'is_game_won': game.check_game_win()}

def get_game() -> Game:
    session_game = session.get('game', None)
    if session_game is None: return
    return pickle.loads(session_game)

def store_game_in_session(game: Game) -> None:
    session['game'] = pickle.dumps(game)

@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def root():
    game = Game()
    store_game_in_session(game)
    print(session)
    
    return jsonify(get_default_return(game))


@app.route('/guess', methods=['GET'])
@cross_origin(supports_credentials=True)
def guess():
    print(session)
    game = get_game()
    if game is None: return 'game not started', 404

    guess_letter = request.args.get('guess_letter', None)
    if guess_letter is None: return 'no guess', 404

    is_correct = game.check_guess(guess_letter)
    if is_correct: game.update()
    
    store_game_in_session(game)

    return get_default_return(game)


app.run(host='localhost', port=5000)
