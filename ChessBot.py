import copy
import random
from datetime import datetime
import sys
import threading


class ChessBot:

    def __init__(self,board):
        self.board = board
        self.RAMIFICATION_FACTOR = 100
        self.NUM_THREADS = 4

    class Node:
        def __init__(self, board, value):
            self.board=board
            self.value=value

    def evaluation(self, board):
        value = 0
        for pice in self.board.white_pices:
            value += pice.value
        for pice in self.board.black_pices:
            value -= pice.value
        return value

    def get_neightbor(self, new_board, side):
        current_board = copy.deepcopy(new_board)
        if side == 'white':
            pices = current_board.white_pices
        else:
            pices = current_board.black_pices
        random.seed(datetime.now())
        moves = pices[random.randint(0,len(pices)-1)].get_possible_moves(current_board.board)
        if moves:
            move = moves[random.randint(0,len(moves)-1)]
            current_board.movePice(move)
        return current_board

    def bot_move(self):
        
        threads_response=[]
        charge = self.charge_balance()
        
        def move_conc(self_charge): 
            boards=[]  
            for j in range(self_charge):
                neightbor=self.get_neightbor(self.board,'black')
                boards.append(self.Node(neightbor,self.minimax(2, False, neightbor, -sys.maxsize, sys.maxsize, self_charge)))
            threads_response.append(min(boards, key = lambda t: t.value))
        
        
        threads=[threading.Thread(target=move_conc, args=(charge[i],), daemon = True) for i in range(self.NUM_THREADS)]
        for t in range(len(threads)):
            threads[t].start()
        for t in range(len(threads)):
            threads[t].join()
        return min(threads_response, key = lambda t: t.value).board
        
    def charge_balance(self):
        charge_repartition = []
        charge = self.RAMIFICATION_FACTOR//self.NUM_THREADS
        for i in range(self.NUM_THREADS):
            charge_repartition.append(charge)
        for i in range(self.RAMIFICATION_FACTOR%self.NUM_THREADS):
            charge_repartition[i%self.NUM_THREADS] += 1
        return charge_repartition

    def minimax(self, depth, maxTurn, board, alpha, beta, self_charge):
        current_board = copy.deepcopy(board)
        if depth == 0 or not current_board.check_kings_alive():
            return self.evaluation(current_board.board)
        if maxTurn:
            maxEval = -sys.maxsize
            for i in range(self_charge):
                eval = self.minimax(depth - 1, False, self.get_neightbor(current_board,'white'), alpha, beta, self_charge)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = +sys.maxsize
            for i in range(self_charge):
                eval = self.minimax(depth - 1, True, self.get_neightbor(current_board,'black'), alpha, beta, self_charge)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval