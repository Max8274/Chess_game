from abc import ABC
import chess

"""A generic utility class"""
class Utility(ABC):

    #the upper left value (first value of the list) is 1a on a chess board, then you have 1b,...
    pawnWhite = [
        0, 0, 0, 0, 0, 0, 0, 0,                   # 1a 1b 1c 1d 1e 1f 1g 1h
        5, 10, 10, -20, -20, 10, 10, 5,           # 2a 2b 2c 2d 2e 2f 2g 2h
        5, -5, -10, 0, 0, -10, -5, 5,             # 3a 3b 3c 3d 3e 3f 3g 3h
        0, 0, 0, 20, 20, 0, 0, 0,                 # 4a 4b 4c 4d 4e 4f 4g 4h
        5, 5, 10, 25, 25, 10, 5, 5,               # 5a 5b 5c 5d 5e 5f 5g 5h
        10, 10, 20, 30, 30, 20, 10, 10,           # 6a 6b 6c 6d 6e 6f 6g 6h
        50, 50, 50, 50, 50, 50, 50, 50,           # 7a 7b 7c 7d 7e 7f 7g 7h
        0, 0, 0, 0, 0, 0, 0, 0]                   # 8a 8b 8c 8d 8e 8f 8g 8h

    bishopWhite = [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20]

    knightWhite = [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50]

    rookWhite = [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0]

    queenWhite = [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 5, 5, 5, 5, 5, 0, -10,
        0, 0, 5, 5, 5, 5, 0, -5,
        -5, 0, 5, 5, 5, 5, 0, -5,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20]

    kingWhite = [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30]
    
    # Determine the value of the current board position (high is good for white, low is good for black, 0 is neutral)

    def board_value(self, board: chess.Board):
        pawnWPlaceScore = sum([self.pawnWhite[i] for i in board.pieces(piece_type=chess.PAWN, color=chess.WHITE)])
        bishopWPlaceScore = sum([self.bishopWhite[i] for i in board.pieces(piece_type=chess.BISHOP, color=chess.WHITE)])
        knightWPlaceScore = sum([self.knightWhite[i] for i in board.pieces(piece_type=chess.KNIGHT, color=chess.WHITE)])
        rookWPlaceScore = sum([self.rookWhite[i] for i in board.pieces(piece_type=chess.ROOK, color=chess.WHITE)])
        queenWPlaceScore = sum([self.queenWhite[i] for i in board.pieces(piece_type=chess.QUEEN, color=chess.WHITE)])
        kingWPlaceScore = sum([self.kingWhite[i] for i in board.pieces(piece_type=chess.KING, color=chess.WHITE)])

        n_white = 0
        n_white += len(board.pieces(piece_type=chess.PAWN, color=chess.WHITE))*10 + pawnWPlaceScore
        n_white += len(board.pieces(piece_type=chess.BISHOP, color=chess.WHITE))*30 +bishopWPlaceScore
        n_white += len(board.pieces(piece_type=chess.KNIGHT, color=chess.WHITE))*30 + knightWPlaceScore
        n_white += len(board.pieces(piece_type=chess.ROOK, color=chess.WHITE))*50 + rookWPlaceScore
        n_white += len(board.pieces(piece_type=chess.QUEEN, color=chess.WHITE))*100 + queenWPlaceScore
        n_white += len(board.pieces(piece_type=chess.KING, color=chess.WHITE))*1000 + kingWPlaceScore

        pawnBPlaceScore = sum([self.pawnWhite[chess.square_mirror(i)] for i in board.pieces(piece_type=chess.PAWN, color=chess.BLACK)])
        bishopBPlaceScore = sum([self.bishopWhite[chess.square_mirror(i)] for i in board.pieces(piece_type=chess.BISHOP, color=chess.BLACK)])
        knightBPlaceScore = sum([self.knightWhite[chess.square_mirror(i)] for i in board.pieces(piece_type=chess.KNIGHT, color=chess.BLACK)])
        rookBPlaceScore = sum([self.rookWhite[chess.square_mirror(i)] for i in board.pieces(piece_type=chess.ROOK, color=chess.BLACK)])
        queenBPlaceScore = sum([self.queenWhite[chess.square_mirror(i)] for i in board.pieces(piece_type=chess.QUEEN, color=chess.BLACK)])
        kingBPlaceScore = sum([self.kingWhite[chess.square_mirror(i)] for i in board.pieces(piece_type=chess.KING, color=chess.BLACK)])

        n_black = 0
        n_black += len(board.pieces(piece_type=chess.PAWN, color=chess.BLACK))*10 + pawnBPlaceScore
        n_black += len(board.pieces(piece_type=chess.BISHOP, color=chess.BLACK))*30 + bishopBPlaceScore
        n_black += len(board.pieces(piece_type=chess.KNIGHT, color=chess.BLACK))*30 + knightBPlaceScore
        n_black += len(board.pieces(piece_type=chess.ROOK, color=chess.BLACK))*50 + rookBPlaceScore
        n_black += len(board.pieces(piece_type=chess.QUEEN, color=chess.BLACK))*100 + queenBPlaceScore
        n_black += len(board.pieces(piece_type=chess.KING, color=chess.BLACK))*1000 + kingBPlaceScore

        return n_white - n_black #black wilt lage value, white een hoge