from flask import Flask, render_template, jsonify, request
import chess
import engine
import random
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game')
def new_game():
    board = chess.Board()
    return jsonify({'board': str(board.fen())})

@app.route('/random_move', methods = ['POST'])
def random_move():
    print(request.data)
    json_post = request.get_json(force=True)
    if ("board" in json_post):
        board = engine.Minmax(json_post['board'])
        board.random_move()
    else:
        board = chess.Board()
    return jsonify({'board': str(board.get_fen())})

@app.route('/best_random_move', methods = ['POST'])
def best_random_move():
    json_post = request.get_json(force = True)
    if ("board" in json_post):
        board = engine.Minmax(json_post['board'])
        uci_move = board.calculate_best_move()
        board.move(uci_move)

    return jsonify({'board': str(board.get_fen())})

if __name__ == '__main__':
    app.run(debug=True)