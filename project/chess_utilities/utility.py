from abc import ABC
import chess

"""A generic utility class"""
class Utility(ABC):
    
    # Determine the value of the current board position (high is good for white, low is good for black, 0 is neutral)

    def board_value(self, board: chess.Board):
        n_white = 0
        n_white += len(board.pieces(piece_type=chess.PAWN, color=chess.WHITE))*1
        n_white += len(board.pieces(piece_type=chess.BISHOP, color=chess.WHITE))*3
        n_white += len(board.pieces(piece_type=chess.KNIGHT, color=chess.WHITE))*3
        n_white += len(board.pieces(piece_type=chess.ROOK, color=chess.WHITE))*5
        n_white += len(board.pieces(piece_type=chess.QUEEN, color=chess.WHITE))*10
        n_white += len(board.pieces(piece_type=chess.KING, color=chess.WHITE))*1000

        n_black = 0
        n_black += len(board.pieces(piece_type=chess.PAWN, color=chess.BLACK))*1
        n_black += len(board.pieces(piece_type=chess.BISHOP, color=chess.BLACK))*3
        n_black += len(board.pieces(piece_type=chess.KNIGHT, color=chess.BLACK))*3
        n_black += len(board.pieces(piece_type=chess.ROOK, color=chess.BLACK))*5
        n_black += len(board.pieces(piece_type=chess.QUEEN, color=chess.BLACK))*10
        n_black += len(board.pieces(piece_type=chess.KING, color=chess.BLACK))*1000
        return n_white - n_black