import chess
import random

def evaluate_board(fen_chess):
    pass

class Minmax(object):
    def __init__(self, fen=chess.Board().fen(), depth = 3, alphabeta = False):
        self.depth = depth
        self.alphabeta = alphabeta
        self.piece_weights = {
            'P': 10,
            'N': 30,
            'B': 30,
            'R': 50,
            'Q': 90,
            'K': 900,
            'p': -10,
            'n': -30,
            'b': -30,
            'r': -50,
            'q': -90,
            'k': -900
        }
        self.score = 0
        self.board = chess.Board(fen)

    def set_board(self, fen):
        self.board = chess.Board(fen)

    def get_fen(self):
        return self.board.fen()

    def random_move(self):
        legal_moves = self.get_legal_moves()
        random_int = random.randint(0,len(legal_moves)-1)

        self.board.push_uci(legal_moves[random_int])

    def get_legal_moves(self):
        '''
        Returns the legal moves in uci format
        '''
        legal_moves = self.board.legal_moves
        possible_moves = []
        for move in legal_moves:
            possible_moves.append(move.uci())

        return possible_moves

    def calculate_best_move(self, fen = False, player = 'white'):
        if not fen:
            fen = self.get_fen()

        if player == 'white':
            score = 9999

        for move in self.get_legal_moves():
            board = self.board.copy()
            board.push_uci(move)
            new_score = self.calculate_score(board.fen())
            if new_score < score:
                score = new_score
                best_move = move

        return best_move

    def calculate_score(self, fen = False):
        if not fen:
            fen = self.get_fen()

        score = 0
        rows = fen.split()[0].split('/')
        for row in rows:
            for char in list(row):
                if char in self.piece_weights:
                    score += self.piece_weights[char]

        return score

    def move(self, uci):
        self.board.push_uci(uci)


