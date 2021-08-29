from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from hangman import Game

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def root():
    game = Game()
    return jsonify({'total_letters': game.total_letters, 'tip': game.tip, 'current_game': str(game)})


app.run(host='localhost', port=5000)
