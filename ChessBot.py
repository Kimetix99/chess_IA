import copy
import random
from datetime import datetime

class ChessBot:

    def __init__(self, board):
        self.board = board

    def evaluation(self, board):
        value = 0
        for row in board:
            for cell in row:
                if cell['p'] != '':
                    if cell['p'].side == 'black':
                        value -= cell['p'].value
                    else:
                        value += cell['p'].value
        return value
            

    def get_neightbor(self, moves, new_board, value):
        random.seed(datetime.now())
        new_board.move_to_destination(moves[random.randint(0,len(moves))])
        new_value = self.evaluation(new_board.board)
        return new_board, new_value

    def random_pice(self):
        value = self.evaluation(self.board.board)
        board = copy.copy(self.board)
        pices = self.board.black_pices
        random.seed(datetime.now())
        moves = pices[random.randint(0,len(pices))]['p'].get_possible_moves(board.board)
        new_board, new_value = self.get_neightbor(moves, board, value)
        return new_board, new_value

    def minimax(self, target_depth, curr_depth, maxTurn, optimal_board, optimal_value):
        if curr_depth == target_depth:
            return optimal_board
        for i in range(0,10):
            new_board, new_value = self.random_pice()
            if maxTurn:
                if new_value > optimal_value:
                    optimal_value = new_value
                    optimal_board = new_board
                return self.minimax(target_depth, curr_depth + 1, False, optimal_board, optimal_value)  
            else:
                if new_value < optimal_value:
                    optimal_value = new_value
                    optimal_board = new_board
                return self.minimax(target_depth, curr_depth + 1, False, optimal_board, optimal_value) 
            
        
        

