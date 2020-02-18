import copy
import random
from datetime import datetime
import sys


class ChessBot:

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

    def get_neightbor(self, new_board):
        pices = new_board.get_black_pices()
        random.seed(datetime.now())
        moves = pices[random.randint(0,len(pices)-1)]['p'].get_possible_moves(new_board.board)
        if moves:
            move = moves[random.randint(0,len(moves)-1)]
            new_board.move_to_destination(move)
        return new_board

    def bot_move(self,board):
        boards=[]
        for i in range(100):
            neightbor=self.get_neightbor(board)
            boards.append((neightbor, self.minimax(3, False, neightbor)))
        print(boards)

    def minimax(self, depth, maxTurn, board):
        if depth == 0 or not board.check_kings_alive():
            return self.evaluation(board.board)
        if maxTurn:
            maxEval = -sys.maxsize
            for i in range(100):
                eval = self.minimax(depth - 1, False, self.get_neightbor(board))
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = +sys.maxsize
            for i in range(100):
                eval = self.minimax(depth - 1, True, self.get_neightbor(board))
                minEval = min(minEval, eval)
            return minEval

            
            
        
        

