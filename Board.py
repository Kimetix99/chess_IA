from Pices.BlackPiceFactory import BlackPiceFactory
from Pices.WhitePiceFactory import WhitePiceFactory
import math

class Board:

    def __init__(self):
        self.black_factory = BlackPiceFactory()
        self.white_factory = WhitePiceFactory()
        self.board=[
            [{"p":self.black_factory.create_tower(0,0),"m":""},{"p":self.black_factory.create_horse(0,1),"m":""},{"p":self.black_factory.create_bishop(0,2),"m":""},{"p":self.black_factory.create_queen(0,3),"m":""},{"p":self.black_factory.create_king(0,4),"m":""},{"p":self.black_factory.create_bishop(0,5),"m":""},{"p":self.black_factory.create_horse(0,6),"m":""},{"p":self.black_factory.create_tower(0,7),"m":""}],
            [{"p":self.black_factory.create_pawn(1,0),"m":""},{"p":self.black_factory.create_pawn(1,1),"m":""},{"p":self.black_factory.create_pawn(1,2),"m":""},{"p":self.black_factory.create_pawn(1,3),"m":""},{"p":self.black_factory.create_pawn(1,4),"m":""},{"p":self.black_factory.create_pawn(1,5),"m":""},{"p":self.black_factory.create_pawn(1,6),"m":""},{"p":self.black_factory.create_pawn(1,7),"m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":self.white_factory.create_pawn(6,0),"m":""},{"p":self.white_factory.create_pawn(6,1),"m":""},{"p":self.white_factory.create_pawn(6,2),"m":""},{"p":self.white_factory.create_pawn(6,3),"m":""},{"p":self.white_factory.create_pawn(6,4),"m":""},{"p":self.white_factory.create_pawn(6,5),"m":""},{"p":self.white_factory.create_pawn(6,6),"m":""},{"p":self.white_factory.create_pawn(6,7),"m":""}],
            [{"p":self.white_factory.create_tower(7,0),"m":""},{"p":self.white_factory.create_horse(7,1),"m":""},{"p":self.white_factory.create_bishop(7,2),"m":""},{"p":self.white_factory.create_queen(7,3),"m":""},{"p":self.white_factory.create_king(7,4),"m":""},{"p":self.white_factory.create_bishop(7,5),"m":""},{"p":self.white_factory.create_horse(7,6),"m":""},{"p":self.white_factory.create_tower(7,7),"m":""}]
        ]
        self.black_pices=[]
        top_side=self.board[0] + self.board[1]
        for cell in top_side:
            self.black_pices.append(cell['p'])
        self.white_pices=[]
        bot_side=self.board[6] + self.board[7]
        for cell in bot_side:
            self.white_pices.append(cell['p'])
        self.black_king_alive=True
        self.white_king_alive=True

    def containsPlayerPice(self, posX, posY, turn):
        return self.board[posY][posX]['p'] != '' and self.board[posY][posX]['p'].side == turn.side

    def isMoveCell(self,posX,posY):
        return self.board[posY][posX]['m'] != ''
    
    def actualizeMoves(self, posX, posY):
        moves = self.board[posY][posX]['p'].get_possible_moves(self.board)
        for move in moves:
            self.board[move.destination[1]][move.destination[0]]['m'] = move
            
    def movePice(self, move):
        if self.board[move.destination[1]][move.destination[0]]['p'] == '':
            self.replace_pice(move)
            self.check_init_pos(move)
        else:
            if move.enrock:
                self.exchange_pice(move)
            else:
                self.kill_pice(move)
                self.replace_pice(move)
                self.check_init_pos(move)
        
    def kill_pice(self, move):
        if self.board[move.destination[1]][move.destination[0]]['p'].side == 'black':
            self.black_pices.remove(self.board[move.destination[1]][move.destination[0]]['p'])
        else:
            self.white_pices.remove(self.board[move.destination[1]][move.destination[0]]['p'])

    def check_init_pos(self, move):
        if self.board[move.destination[1]][move.destination[0]]['p'].is_pawn() or self.board[move.destination[1]][move.destination[0]]['p'].is_tower() or self.board[move.destination[1]][move.destination[0]]['p'].is_king():
            if self.board[move.destination[1]][move.destination[0]]['p'].init_pos:
                self.board[move.destination[1]][move.destination[0]]['p'].init_pos = False

    def exchange_pice(self, move):
        posX = self.get_king_pos(move)
        self.board[move.origin[1]][posX]['p']=self.board[move.origin[1]][move.origin[0]]['p']
        self.board[move.origin[1]][posX]['p'].posX = posX
        self.board[move.origin[1]][posX]['p'].init_pos = False
        if posX == 1 or posX == 2:
            self.board[move.destination[1]][posX+1]['p'] = self.board[move.destination[1]][move.destination[0]]['p']
            self.board[move.origin[1]][posX+1]['p'].posX = posX+1
            self.board[move.destination[1]][posX+1]['p'].init_pos = False
        else:
            self.board[move.destination[1]][posX-1]['p'] = self.board[move.destination[1]][move.destination[0]]['p']
            self.board[move.origin[1]][posX-1]['p'].posX = posX-1
            self.board[move.destination[1]][posX-1]['p'].init_pos = False
        self.board[move.origin[1]][move.origin[0]]['p'] = ''
        self.board[move.destination[1]][move.destination[0]]['p'] = ''
        
    def replace_pice(self, move):
        if self.pawn_reaches_final(move):
            if self.is_white_pice(move):
                self.white_pices.remove(self.board[move.origin[1]][move.origin[0]]['p'])
                newQueen = self.white_factory.create_queen(move.origin[1],move.origin[0])
                self.board[move.origin[1]][move.origin[0]]['p'] = newQueen
                self.white_pices.append(newQueen)
            else:
                self.black_pices.remove(self.board[move.origin[1]][move.origin[0]]['p'])
                newQueen = self.black_factory.create_queen(move.origin[1],move.origin[0])
                self.board[move.origin[1]][move.origin[0]]['p'] = newQueen
                self.white_pices.append(newQueen)
        if self.king_dies(move):
            if self.is_white_king(move):
                self.white_king_alive = False
            else:
                self.black_king_alive = False
        self.board[move.destination[1]][move.destination[0]]['p'] = self.board[move.origin[1]][move.origin[0]]['p']
        self.board[move.destination[1]][move.destination[0]]['p'].posX=move.destination[0]
        self.board[move.destination[1]][move.destination[0]]['p'].posY=move.destination[1]
        self.board[move.origin[1]][move.origin[0]]['p'] = ''

    def is_white_pice(self, move):
        return self.board[move.origin[1]][move.origin[0]]['p'] != '' and self.board[move.origin[1]][move.origin[0]]['p'].side == 'white'

    def pawn_reaches_final(self, move):
        return ((move.destination[1] == 7 and self.board[move.origin[1]][move.origin[0]]['p'].is_pawn() and self.board[move.origin[1]][move.origin[0]]['p'].side == 'black')
                or (move.destination[1] == 0 and self.board[move.origin[1]][move.origin[0]]['p'].is_pawn() and self.board[move.origin[1]][move.origin[0]]['p'].side == 'white'))

    def check_kings_alive(self):
        return self.black_king_alive and self.white_king_alive

    def king_dies(self, move):
        return self.board[move.destination[1]][move.destination[0]]['p'] != '' and self.board[move.destination[1]][move.destination[0]]['p'].is_king()

    def is_white_king(self, move):
        return self.board[move.destination[1]][move.destination[0]]['p'].side == 'white'
    
    def get_king_pos(self,move):
        if self.board[move.origin[1]][move.origin[0]]['p'].side == 'black':
            return math.ceil((move.origin[0]+move.destination[0])/2)
        else:
            return math.ceil((move.origin[0]+move.destination[0])/2)