from tkinter import *
from Board import *
from Game import *
from ChessBot import *
import math 


class Chess:

    def __init__(self,window):
        self.window=window
        self.BOARD_HEIGHT = 480
        self.BOARD_WIDTH = 480
        self.NUM_X_CELLS = 8
        self.NUM_Y_CELLS = 8
        self.board=Canvas(window, height=self.BOARD_HEIGHT, width=self.BOARD_WIDTH)
        self.cell_height = self.BOARD_HEIGHT/self.NUM_Y_CELLS
        self.cell_width = self.BOARD_WIDTH/self.NUM_X_CELLS
        self.images=[]

    #Create board
    def create_board(self):
        
        current_height = 0
        current_width = 0

        for i in range (0,self.NUM_Y_CELLS):
            for j in range (0,self.NUM_X_CELLS):
                if i%2 == 0:
                    if j%2 == 0:
                        self.board.create_rectangle(current_width, current_height, current_width+self.cell_width, current_height+self.cell_height, fill="#61b0ff")
                    else:
                        self.board.create_rectangle(current_width, current_height, current_width+self.cell_width, current_height+self.cell_height, fill="#ff9661")
                else:
                    if j%2==0:
                        self.board.create_rectangle(current_width, current_height, current_width+self.cell_width, current_height+self.cell_height, fill="#ff9661")
                    else:
                        self.board.create_rectangle(current_width, current_height, current_width+self.cell_width, current_height+self.cell_height, fill="#61b0ff")
                current_width += self.cell_width
            current_height += self.cell_height
            current_width = 0
        self.board.pack()
              

    def display_pices(self,board):
        i = 1
        for row in board.board:
            j = 1
            for pice in row:
                if pice["m"] != "" and pice["p"]== "":
                    self.board.create_rectangle(self.x_coordinates_to_size(j)-((self.BOARD_WIDTH/self.NUM_X_CELLS)/2),self.y_coordinates_to_size(i)-((self.BOARD_HEIGHT/self.NUM_Y_CELLS)/2), self.x_coordinates_to_size(j)+self.cell_width-((self.BOARD_WIDTH/self.NUM_X_CELLS)/2), self.y_coordinates_to_size(i)+self.cell_height-((self.BOARD_HEIGHT/self.NUM_Y_CELLS)/2), fill="#00FF3A")
                elif pice['p'] == "" and pice['m'] == "":
                    pass
                elif pice["p"] != "" and pice["m"] == "":
                    self.images.append(PhotoImage(file=pice["p"].figure))
                    self.board.create_image(self.x_coordinates_to_size(j),self.y_coordinates_to_size(i),image=self.images[-1])
                else:
                    self.board.create_rectangle(self.x_coordinates_to_size(j)-((self.BOARD_WIDTH/self.NUM_X_CELLS)/2),self.y_coordinates_to_size(i)-((self.BOARD_HEIGHT/self.NUM_Y_CELLS)/2), self.x_coordinates_to_size(j)+self.cell_width-((self.BOARD_WIDTH/self.NUM_X_CELLS)/2), self.y_coordinates_to_size(i)+self.cell_height-((self.BOARD_HEIGHT/self.NUM_Y_CELLS)/2), fill="#00FF3A")
                    self.images.append(PhotoImage(file=pice["p"].figure))
                    self.board.create_image(self.x_coordinates_to_size(j),self.y_coordinates_to_size(i),image=self.images[-1])
                j+=1  
            i += 1
        self.board.pack()
    
    def x_coordinates_to_size(self,x):
        return (x*(self.BOARD_WIDTH/self.NUM_X_CELLS))-((self.BOARD_WIDTH/self.NUM_X_CELLS)/2)
                
    def y_coordinates_to_size(self,y):
        return (y*(self.BOARD_HEIGHT/self.NUM_Y_CELLS))-((self.BOARD_HEIGHT/self.NUM_Y_CELLS)/2)

    def size_to_x_coordinates(self,sizeX):
        return math.ceil(sizeX/(self.BOARD_WIDTH/self.NUM_X_CELLS))-1

    def size_to_y_coordinates(self,sizeY):
        return math.ceil(sizeY/(self.BOARD_HEIGHT/self.NUM_Y_CELLS))-1
        

if __name__ == "__main__":
    window = Tk()
    window.title("Chess")
    chess = Chess(window)
    chess.create_board()
    board = Board()
    chess.display_pices(board)
    game=Game(chess,board)
    game.start_game()
    window.mainloop()