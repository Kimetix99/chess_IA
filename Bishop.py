from Pice import Pice
from Move import Move

class Bishop(Pice):
    
    def __init__(self, id, side, figure, alive, posY, posX):
        super(Bishop, self).__init__(id, side, figure, alive, posY, posX)

    def get_possible_moves(self, board):
        moves=[]
        self.move_up_left(moves, board)
        self.move_up_right(moves, board)
        self.move_down_left(moves, board)
        self.move_down_right(moves, board)
        return moves
        
    def move_up_left(self, moves, board):
        next_posY = self.posY-1
        next_posX = self.posX-1
        while next_posY >= 0 and next_posX >= 0 and board[next_posY][next_posX]['p'] == '':
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            next_posY-=1
            next_posX-=1
        if next_posY >= 0 and next_posX >= 0 and board[next_posY][next_posX]['p'] != '' and board[next_posY][next_posX]['p'].side != self.side:
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_up_right(self, moves, board):
        next_posY = self.posY-1
        next_posX = self.posX+1
        while next_posY >= 0 and next_posX <= 7 and board[next_posY][next_posX]['p'] == '':
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            next_posY-=1
            next_posX+=1
        if next_posY >= 0 and next_posX <= 7 and board[next_posY][next_posX]['p'] != '' and board[next_posY][next_posX]['p'].side != self.side:
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))

    def move_down_left(self, moves, board):
        next_posY = self.posY+1
        next_posX = self.posX-1
        while next_posY <= 7 and next_posX >= 0 and board[next_posY][next_posX]['p'] == '':
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            next_posY+=1
            next_posX-=1
        if next_posY <= 7 and next_posX >= 0 and board[next_posY][next_posX]['p'] != '' and board[next_posY][next_posX]['p'].side != self.side:
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
    
    def move_down_right(self, moves, board):
        next_posY = self.posY+1
        next_posX = self.posX+1
        while next_posY <= 7 and next_posX <= 7 and board[next_posY][next_posX]['p'] == '':
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))
            next_posY+=1
            next_posX+=1
        if next_posY <= 7 and next_posX <= 7 and board[next_posY][next_posX]['p'] != '' and board[next_posY][next_posX]['p'].side != self.side:
            moves.append(Move((self.posX,self.posY),(next_posX,next_posY),False))