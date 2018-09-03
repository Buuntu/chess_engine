from flask import Flask, render_template, jsonify, request
import chess
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
    # json_post = json.loads(request.data)
    if ("board" in json_post):
        board = chess.Board(json_post['board'])
        # board.turn = False
        legal_moves = board.legal_moves
        random_int = random.randint(0,legal_moves.count()-1)
        possible_moves = []
        for move in legal_moves:
            possible_moves.append(move)

        print(legal_moves)
        
        print(possible_moves[random_int])
        move = possible_moves[random_int]
        #move = chess.Move.from_uci(possible_moves[random_int])
        board.push_uci(move.uci())
    else:
        board = chess.Board()
    return jsonify({'board': str(board.fen())})

if __name__ == '__main__':
    app.run(debug=True)