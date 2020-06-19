from Pices.PiceFactory import PiceFactory
from Pices.Types.Bishop import Bishop
from Pices.Types.Horse import Horse
from Pices.Types.King import King
from Pices.Types.Pawn import Pawn
from Pices.Types.Queen import Queen
from Pices.Types.Tower import Tower

class WhitePiceFactory(PiceFactory):

    def create_pawn(self,y,x):
        return Pawn("pawn","white","./static/img/white_p.png",True,y,x)

    def create_tower(self,y,x):
        return Tower("tower","white","./static/img/white_t.png",True,y,x)

    def create_horse(self,y,x):
        return Horse("horse","white","./static/img/white_h.png",True,y,x)

    def create_bishop(self,y,x):
        return Bishop("bishop","white","./static/img/white_b.png",True,y,x)

    def create_queen(self,y,x):
        return Queen("queen", "white","./static/img/white_q.png",True,y,x)

    def create_king(self,y,x):
        return King("king","white","./static/img/white_k.png",True,y,x)