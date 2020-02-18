from tkinter import *
from Pice import Pice
from Tower import Tower
from Bishop import Bishop
from Pawn import Pawn
from King import King
from Queen import Queen
from Horse import Horse
from Move import Move
import math

class Board:

    def __init__(self):
        self.board=[
            [{"p":Tower("tower","black",PhotoImage(file="./img/black_t.png"),True,0,0),"m":""},{"p":Horse("horse","black",PhotoImage(file="./img/black_h.png"),True,0,1),"m":""},{"p":Bishop("bishop","black",PhotoImage(file="./img/black_b.png"),True,0,2),"m":""},{"p":Queen("queen", "black",PhotoImage(file="./img/black_q.png"),True,0,3),"m":""},{"p":King("king","black",PhotoImage(file="./img/black_k.png"),True,0,4),"m":""},{"p":Bishop("bishop","black",PhotoImage(file="./img/black_b.png"),True,0,5),"m":""},{"p":Horse("horse","black",PhotoImage(file="./img/black_h.png"),True,0,6),"m":""},{"p":Tower("tower","black",PhotoImage(file="./img/black_t.png"),True,0,7),"m":""}],
            [{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,0),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,1),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,2),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,3),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,4),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,5),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,6),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,7),"m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,0),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,1),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,2),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,3),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,4),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,5),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,6),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,7),"m":""}],
            [{"p":Tower("tower","white",PhotoImage(file="./img/white_t.png"),True,7,0),"m":""},{"p":Horse("horse","white",PhotoImage(file="./img/white_h.png"),True,7,1),"m":""},{"p":Bishop("bishop","white",PhotoImage(file="./img/white_b.png"),True,7,2),"m":""},{"p":Queen("queen", "white",PhotoImage(file="./img/white_q.png"),True,7,3),"m":""},{"p":King("king","white",PhotoImage(file="./img/white_k.png"),True,7,4),"m":""},{"p":Bishop("bishop","white",PhotoImage(file="./img/white_b.png"),True,7,5),"m":""},{"p":Horse("horse","white",PhotoImage(file="./img/white_h.png"),True,7,6),"m":""},{"p":Tower("tower","white",PhotoImage(file="./img/white_t.png"),True,7,7),"m":""}]
        ]
        self.black_pices=self.board[0] + self.board[1]
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
            
    def movePice(self, posX, posY):
        move = self.board[posY][posX]['m']
        self.move_to_destination(move)
        
    def move_to_destination(self, move):
        if move.enrock:
            self.exchange_pice(move)
        else:
            self.replace_pice(move)
            self.check_init_pos(move)

    def check_init_pos(self, move):
        if isinstance(self.board[move.destination[1]][move.destination[0]]['p'],Pawn) or isinstance(self.board[move.destination[1]][move.destination[0]]['p'],Tower) or isinstance(self.board[move.destination[1]][move.destination[0]]['p'],King):
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
            self.board[move.origin[1]][move.origin[0]]['p'] = Queen("queen", self.board[move.origin[1]][move.origin[0]]['p'].side, PhotoImage(file="./img/"+self.board[move.origin[1]][move.origin[0]]['p'].side+"_q.png"),True,move.origin[1],move.origin[0])
        if self.king_dies(move):
            if self.is_white_king(move):
                self.white_king_alive = False
            else:
                self.black_king_alive = False
        self.board[move.destination[1]][move.destination[0]]['p'] = self.board[move.origin[1]][move.origin[0]]['p']
        self.board[move.destination[1]][move.destination[0]]['p'].posX=move.destination[0]
        self.board[move.destination[1]][move.destination[0]]['p'].posY=move.destination[1]
        self.board[move.origin[1]][move.origin[0]]['p'] = ''

    def pawn_reaches_final(self, move):
        return ((move.destination[1] == 7 and isinstance(self.board[move.origin[1]][move.origin[0]]['p'],Pawn) and self.board[move.origin[1]][move.origin[0]]['p'].side == 'black') 
                or (move.destination[1] == 0 and isinstance(self.board[move.origin[1]][move.origin[0]]['p'],Pawn) and self.board[move.origin[1]][move.origin[0]]['p'].side == 'white'))

    def check_kings_alive(self):
        return self.black_king_alive and self.white_king_alive

    def king_dies(self, move):
        return isinstance(self.board[move.destination[1]][move.destination[0]]['p'], King)

    def is_white_king(self, move):
        return self.board[move.destination[1]][move.destination[0]]['p'].side == 'white'
    
    def get_king_pos(self,move):
        if self.board[move.origin[1]][move.origin[0]]['p'].side == 'black':
            return math.ceil((move.origin[0]+move.destination[0])/2)
        else:
            return math.floor((move.origin[0]+move.destination[0])/2)
    
    def get_black_pices(self):
        black_pices=[]
        for row in self.board:
            for cell in row:
                if cell['p'] != '' and cell['p'].side=='black':
                    black_pices.append(cell)
        return black_pices