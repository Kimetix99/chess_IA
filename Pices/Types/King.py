from Pices.Pice import Pice
from Utils.Move import Move
import sys


class King(Pice):
    
    def __init__(self, id, side, figure, alive, posY, posX):
        super(King, self).__init__(id, side, figure, alive, posY, posX)
        self.init_pos = True
        self.value = sys.maxsize

    def get_possible_moves(self, board):
        moves=[]
        self.move_up(moves, board)
        self.move_left(moves, board)
        self.move_right(moves, board)
        self.move_down(moves, board)
        self.move_up_left(moves, board)
        self.move_up_right(moves, board)
        self.move_down_left(moves, board)
        self.move_down_right(moves, board)
        self.enrock(moves, board)
        return moves

    def move_up(self, moves, board):
        next_posY = self.posY-1
        if next_posY >= 0:
            if board[next_posY][self.posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(self.posX,next_posY),False))
            else:
                if board[next_posY][self.posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(self.posX,next_posY),False))

    def move_left(self, moves, board):
        next_posX = self.posX-1
        if next_posX >= 0:
            if board[self.posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,self.posY),False))
            else:
                if board[self.posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,self.posY),False))

    def move_right(self, moves, board):
        next_posX = self.posX+1
        if next_posX <= 7:
            if board[self.posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,self.posY),False))
            else:
                if board[self.posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,self.posY),False))

    def move_down(self, moves, board):
        next_posY = self.posY+1
        if next_posY <= 7:
            if board[next_posY][self.posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(self.posX,next_posY),False))
            else:
                if board[next_posY][self.posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(self.posX,next_posY),False))
        
    def move_up_left(self, moves, board):
        next_posX = self.posX-1
        next_posY = self.posY-1
        if next_posX >= 0 and next_posY >= 0:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
        

    def move_up_right(self, moves, board):
        next_posX = self.posX+1
        next_posY = self.posY-1
        if next_posX <= 7 and next_posY >= 0:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_down_left(self, moves, board):
        next_posX = self.posX-1
        next_posY = self.posY+1
        if next_posX >= 0 and next_posY <= 7:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
        
    
    def move_down_right(self, moves, board):
        next_posX = self.posX+1
        next_posY = self.posY+1
        if next_posX <= 7 and next_posY <= 7:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
    
    def enrock(self, moves, board):
        self.enrock_left_tower(moves, board)
        self.enrock_right_tower(moves, board)

    def enrock_left_tower(self, moves, board):
        next_posX = self.posX-1
        while next_posX >=0 and board[self.posY][next_posX]['p'] == '':
            next_posX-=1
        if next_posX >= 0 and board[self.posY][next_posX]['p'] != '' and board[self.posY][next_posX]['p'].is_tower() and board[self.posY][next_posX]['p'].init_pos and board[self.posY][self.posX]['p'].init_pos:
            moves.append(Move((self.posX,self.posY),(next_posX,self.posY),True))
    
    def enrock_right_tower(self, moves, board):
        next_posX = self.posX+1
        while next_posX <= 7 and board[self.posY][next_posX]['p'] == '':
            next_posX+=1
        if next_posX <= 7 and board[self.posY][next_posX]['p'] != '' and board[self.posY][next_posX]['p'].is_tower() and board[self.posY][next_posX]['p'].init_pos and board[self.posY][self.posX]['p'].init_pos:
            moves.append(Move((self.posX,self.posY),(next_posX,self.posY),True))

    def is_king(self):
        return True