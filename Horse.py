#!/usr/bin/pypy
from Pice import Pice
from Move import Move

class Horse(Pice):
    
    def __init__(self, id, side, figure, alive, posY, posX):
        super(Horse, self).__init__(id, side, figure, alive, posY, posX)
        self.value = 3

    def get_possible_moves(self, board):
        moves=[]
        self.move_up_left(moves, board)
        self.move_up_right(moves, board)
        self.move_down_left(moves, board)
        self.move_down_right(moves, board)
        self.move_left_up(moves, board)
        self.move_right_up(moves, board)
        self.move_left_down(moves, board)
        self.move_right_down(moves, board)
        return moves
        
    def move_up_left(self, moves, board):
        next_posX = self.posX-1
        next_posY = self.posY-2
        if next_posX >= 0 and next_posY >= 0:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_up_right(self, moves, board):
        next_posX = self.posX+1
        next_posY = self.posY-2
        if next_posX <= 7 and next_posY >= 0:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_down_left(self, moves, board):
        next_posX = self.posX-1
        next_posY = self.posY+2
        if next_posX >= 0 and next_posY <= 7:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
        
    
    def move_down_right(self, moves, board):
        next_posX = self.posX+1
        next_posY = self.posY+2
        if next_posX <= 7 and next_posY <= 7:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_left_up(self, moves, board):
        next_posX = self.posX-2
        next_posY = self.posY-1
        if next_posX >= 0 and next_posY >= 0:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_right_up(self, moves, board):
        next_posX = self.posX+2
        next_posY = self.posY-1
        if next_posX <= 7 and next_posY >= 0:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_left_down(self, moves, board):
        next_posX = self.posX-2
        next_posY = self.posY+1
        if next_posX >= 0 and next_posY <= 7:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
        
    def move_right_down(self, moves, board):
        next_posX = self.posX+2
        next_posY = self.posY+1
        if next_posX <= 7 and next_posY <= 7:
            if board[next_posY][next_posX]['p'] == '':
                moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            else:
                if board[next_posY][next_posX]['p'].side != self.side:
                    moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))