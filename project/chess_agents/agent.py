import time
from abc import ABC
import chess
from project.chess_utilities.utility import Utility
import time
import random

import chess
from project.chess_utilities.utility import Utility

"""A generic agent class"""


class Agent(ABC):

    # Initialize your agent with whatever parameters you want
    def __init__(self, utility: Utility, time_limit_move: float) -> None:
        """Setup the Search Agent"""
        self.utility = utility
        self.time_limit_move = 15 #time_limit_move
        self.name = "search agent chesser"
        self.author = "Maxime, Abe, Thijs"



    def max_function(self, board: chess.Board,dept):
        dept = dept -1

        best_utility = -111110
        best_move = None
        for move in list(board.legal_moves):
            #print("move "+ str(move))
            #print("")
            # Play the move
            board.push(move)
            if dept <= 0:
                worst_utility = self.utility.board_value(board)
            else:
                #print(dept)
                worst_utility,worst_move = self.min_function(board,dept)
            if worst_utility > best_utility:
                #print("move beter")
                #print(str(move) +"worsts "+ str(worst_utility) + "best " +str(best_utility))
                best_move = move
                best_utility = worst_utility
            board.pop()
        if best_move == None:
            best_utility = 100000000
        return best_utility,best_move



    def min_function(self, board: chess.Board, dept):
        dept = dept -1
        worst_utility = 100000000000
        worst_move = None
        for move in list(board.legal_moves):

            board.push(move)
            if dept <= 0:
                value = self.utility.board_value(board)
            else:
                #print(dept)
                value,best_move = self.max_function(board,dept)

           # print("move2"+ str(move) +"   value   "+ str(value))
            # If this is better than all other previous moves, store this move and its utility
            if value < worst_utility:
                #print("move2 slechter!!!!"+ str(value))
                worst_move = move
                worst_utility = value
            board.pop()
        if worst_move == None:
            worst_utility = -100000000
        return worst_utility, worst_move

    def calculate_move(self, board: chess.Board):
        if board.turn == chess.WHITE:
            value,move = self.max_function(board,4)
        else:
            value, move = self.min_function(board,3)
        return move
        """
        start_time = time.time()

        # If the agent is playing as black, the utility values are flipped (negative-positive)
        flip_value = 1 if board.turn == chess.WHITE else -1

        #best_move = random.sample(list(board.legal_moves), 1)[0]
        best_utility = -111110

        # Loop trough all legal moves
        for move in list(board.legal_moves):
            print("move "+ str(move))
            print("")
            # Check if the maximum calculation time for this move has been reached
            if time.time() - start_time > self.time_limit_move:
                break
            # Play the move
            board.push(move)
            worst_utility = 1000
            for move2 in list(board.legal_moves):

                board.push(move2)
                value = flip_value * self.utility.board_value(board)
                print("move2"+ str(move2) +"   value   "+ str(value))
                # If this is better than all other previous moves, store this move and its utility
                if value < worst_utility:
                    print("move2 slechter!!!!"+ str(value))
                    worst_move = move2
                    worst_utility = value
                board.pop()

            # If this is better than all other previous moves, store this move and its utility
            if worst_utility > best_utility:
                print("move beter")
                print(str(move) +"worsts "+ str(worst_utility) + "best " +str(best_utility))
                best_move = move
                best_utility = worst_utility

            # Revert the board to its original state
            board.pop()
            
        return best_move
"""
