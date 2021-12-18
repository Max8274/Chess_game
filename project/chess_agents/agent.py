from abc import ABC
import chess
from project.chess_utilities.utility import Utility
import time

"""A generic agent class"""


class Agent(ABC):

    def __init__(self, utility: Utility, time_limit_move: float) -> None:
        """Setup the Search Agent"""
        self.utility = utility
        self.time_limit_move = 15
        self.start_time = 0
        self.no_time_anymore = False
        self.is_max_player = False
        self.name = "Search agent MAT" #MAT = Maxime Abe Thijs
        self.author = "Maxime, Abe, Thijs"

    def minimaxWithPruning(self, board, depth, is_max_player, alpha, beta):
        depth = depth - 1
        best_move = None

        if depth <= 0:
            return self.utility.board_value(board), best_move

        if is_max_player:
            max_value = float('-inf')
            for move in list(board.legal_moves):
                # Play the move
                board.push(move)
                current_value, current_move = self.minimaxWithPruning(board, depth, False, alpha, beta)
                if current_value > max_value:
                    best_move = move
                    max_value = current_value
                if current_value > alpha:
                    alpha = current_value
                #pruning
                if beta <= alpha:
                    break
                # Revert the board to its original state
                board.pop()
            return max_value, best_move

        else:
            min_value = float('inf')
            for move in list(board.legal_moves):
                # Play the move
                board.push(move)
                current_value, current_move = self.minimaxWithPruning(board, depth, True, alpha, beta)
                if current_value < min_value:
                    best_move = move
                    min_value = current_value
                if current_value < beta:
                    beta = current_value
                #pruning
                if beta <= alpha:
                    break
                # Revert the board to its original state
                board.pop()
            return min_value, best_move

    def calculate_move(self, board: chess.Board):
        if board.turn == chess.WHITE:
            self.is_max_player = True
            #self.start_time = time.time()
            value,move = self.minimaxWithPruning(board, 4, self.is_max_player, float('-inf'), float('inf'))
        else:
            self.is_max_player = False
            #self.start_time = time.time()
            value, move = self.minimaxWithPruning(board, 3, self.is_max_player, float('inf'), float('-inf'))
        #self.start_time = 0
        #self.no_time_anymore = False
        return move
"""
    def calculate_move(self, board: chess.Board):
        global best_move
        start_time = time.time()

        # If the agent is playing as black, the utility values are flipped (negative-positive)
        flip_value = -1 if board.turn == chess.WHITE else 1

        best_utility = 0
        # Loop trough all legal moves
        for move in list(board.legal_moves):
            # Check if the maximum calculation time for this move has been reached
            if time.time() - start_time > self.time_limit_move:
                break
            # Play the move
            board.push(move)

            # Determine the value of the board after this move
            value = flip_value * self.utility.board_value(board)
            # If this is better than all other previous moves, store this move and its utility
            if value > best_utility:
                best_move = move
                best_utility = value
            # Revert the board to its original state
            board.pop()
        return best_move
"""
