from Pice import Pice
from Move import Move

class Pawn(Pice):
    
    def __init__(self, id, side, figure, alive, posY, posX):
        super(Pawn, self).__init__(id, side, figure, alive, posY, posX)
        self.init_pos=True

    def get_possible_moves(self, board):
        moves=[]
        self.move_forward(moves, board)
        self.kill_move(moves, board)
        return moves

    def move_forward(self, moves, board):
            if self.init_pos:
                if self.empty_cell(board, self.posX, self.check_side(2)) and self.empty_cell(board, self.posX, self.check_side(1)):
                    moves.append(Move((self.posX, self.posY), (self.posX, self.check_side(2)),False))
                if self.empty_cell(board, self.posX, self.check_side(1)):
                    moves.append(Move((self.posX, self.posY), (self.posX, self.check_side(1)),False))
            else:
                if self.in_board(board) and self.empty_cell(board, self.posX, self.check_side(1)):
                    moves.append(Move((self.posX,self.posY), (self.posX,self.check_side(1)),False))

    def kill_move(self, moves, board):
        if self.in_board(board) and self.can_kill_left(board):
            moves.append(Move((self.posX, self.posY), (self.posX-1, self.check_side(1)),False))
        if self.in_board(board) and self.can_kill_right(board):
            moves.append(Move((self.posX, self.posY), (self.posX+1, self.check_side(1)),False))

    def can_kill_left(self, board):
        return self.posX != 0 and board[self.check_side(1)][self.posX-1]['p'] != '' and self.side != board[self.check_side(1)][self.posX-1]['p'].side

    def can_kill_right(self, board):
        return self.posX != 7 and board[self.check_side(1)][self.posX+1]['p'] != '' and self.side != board[self.check_side(1)][self.posX+1]['p'].side
    
    def check_side(self, value):
        if self.side == 'black': 
            return self.posY+value 
        else: 
            return self.posY-value 
       
    def empty_cell(self, board, posX, posY):
        return board[posY][posX]['p'] == ''
    
    def in_board(self, board):
        return self.check_side(1) <= 7 and self.check_side(1)>=0
