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
    deltaTime = 0.1
    # Initialize your agent with whatever parameters you want
    def __init__(self, utility: Utility, time_limit_move: float) -> None:
        """Setup the Search Agent"""
        self.utility = utility
        self.time_limit_move = time_limit_move
        self.name = "search agent chesser"
        self.author = "Maxime, Abe, Thijs"
        self.deltaTime = 0.01



    def max_function(self, board: chess.Board,dept,alpha, beta,start_time):
        if(time.time()-start_time<self.time_limit_move-self.deltaTime):
            dept = dept -1
            best_utility = -float('inf')
            moves = list(board.legal_moves)
            if len(moves)>0:
                best_move = moves[0]
            else:
                best_move = None
                best_utility =-10000
            if dept <= 0:
                currentValue = self.utility.board_value(board)
                return currentValue,best_move


            for move in moves:
                board.push(move)

                currentValue,worst_move = self.min_function(board,dept, alpha, beta, start_time)
                #if (worst_move == None) & board.is_stalemate():
                #    best_utility = 100000000
                if currentValue > best_utility:
                    best_move = move
                    best_utility = currentValue
                if currentValue> alpha:
                    alpha = currentValue
                if beta<= alpha:
                    board.pop()
                    return best_utility,best_move
                board.pop()

                """elif worst_move == None:
                    if currentValue>0:
                        best_utility = -100
                    else:
                        best_utility = 100"""
        else:
            best_utility = -float('inf')
            best_move = None
        return best_utility,best_move



    def min_function(self, board: chess.Board, dept, alpha, beta, start_time):
        if(time.time()-start_time<self.time_limit_move-self.deltaTime):
            dept = dept -1
            worst_utility = float('inf')
            moves = list(board.legal_moves)
            if len(moves)>0:
                worst_move = moves[0]
            else:
                worst_move = None
                worst_utility = 10000
            if dept <= 0:
                currentValue = self.utility.board_value(board)
                return currentValue,worst_move
            for move in moves:

                board.push(move)
                currentValue,best_move = self.max_function(board,dept,alpha, beta,start_time)
                #if (best_move == None) & board.is_stalemate():
                 #   worst_utility = -100000000
                if currentValue < worst_utility:
                    worst_move = move
                    worst_utility = currentValue
                if currentValue <beta:
                    beta = currentValue
                if beta<= alpha:
                    board.pop()
                    return worst_utility,worst_move
                board.pop()


                """elif worst_move == None:
                    if currentValue>0:
                        worst_utility = 20
                    else:
                        worst_utility = -20"""
        else:
            worst_utility = float('inf')
            worst_move = None
        return worst_utility, worst_move

    def calculate_move(self, board: chess.Board):
        start_time = time.time()
        nogtijd = True
        dept = 2
        while (nogtijd):
            dept = dept+1
            print("dept" + str(dept))
            if board.turn == chess.WHITE:
                value,move = self.max_function(board,dept,-float('inf'),float('inf'), start_time)
            else:
                value, move = self.min_function(board,dept,-float('inf'),float('inf'),start_time)
            if(time.time()-start_time<self.time_limit_move-self.deltaTime):
                bestMove = move
            else:
                nogtijd = False
            print("value: "+ str(value))
        print("time" + str(time.time()-start_time))
        return bestMove
