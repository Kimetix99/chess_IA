from abc import ABC

class Pice(ABC):

    def __init__(self,id,side,figure,alive,posY,posX):
        self.id=id
        self.side=side
        self.figure=figure
        self.alive=alive
        self.posY=posY
        self.posX=posX

    def get_possible_moves(self, board):
        pass
   
    def is_pawn(self):
        return False

    def is_tower(self):
        return False

    def is_king(self):
        return False