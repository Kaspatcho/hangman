from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from hangman import Game
from secrets import token_bytes
from game_session import get_default_return, get_game_from_session, store_game_in_session

app = Flask(__name__)
app.secret_key = str(token_bytes(16))

# essa config faz com que o fetch entenda que é outro site
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_SAMESITE"] = 'None'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def root():
    game = Game()
    store_game_in_session(game)
    return jsonify(get_default_return(game))


@app.route('/guess', methods=['POST'])
@cross_origin(supports_credentials=True)
def guess():
    print(session)
    game = get_game_from_session()
    if game is None: return 'game not started', 404

    guess_letter = request.args.get('guess_letter', None)
    if guess_letter is None: return 'no guess', 404

    is_correct = game.check_guess(guess_letter)
    if is_correct: game.update()
    
    store_game_in_session(game)

    return get_default_return(game)


@app.route('/gameover', methods=['POST'])
@cross_origin(supports_credentials=True)
def gameover():
    game = get_game_from_session()
    if game is None: return 'game not started', 404

    if game.check_game_over():
        final_message = f'Voce perdeu! a palavra era {game.word}'
        return jsonify({'message': final_message})
    
    return 'O jogo ainda nao acabou!', 400


app.run(host='localhost', port=5000, debug=True)
