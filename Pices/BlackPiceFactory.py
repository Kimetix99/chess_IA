from Pices.PiceFactory import PiceFactory
from Pices.Types.Bishop import Bishop
from Pices.Types.Horse import Horse
from Pices.Types.King import King
from Pices.Types.Pawn import Pawn
from Pices.Types.Queen import Queen
from Pices.Types.Tower import Tower


class BlackPiceFactory(PiceFactory):

    def create_pawn(self,y,x):
        return Pawn("pawn","black","./static/img/black_p.png",True,y,x)

    def create_tower(self,y,x):
        return Tower("tower","black","./static/img/black_t.png",True,y,x)

    def create_horse(self,y,x):
        return Horse("horse","black","./static/img/black_h.png",True,y,x)

    def create_bishop(self,y,x):
        return Bishop("bishop","black","./static/img/black_b.png",True,y,x)

    def create_queen(self,y,x):
        return Queen("queen", "black","./static/img/black_q.png",True,y,x)

    def create_king(self,y,x):
        return King("king","black","./static/img/black_k.png",True,y,x)