from Utils.Player import *
from AI.ChessBot import *

class Game:

    def __init__ (self,chess,board, gamemode):
        self.chess = chess
        self.board = board
        self.gamemode = gamemode
        self.player1 = Player('1','white')
        self.player2 = Player('2','black')
        self.turn = self.player1
        self.chessboot = ChessBot(self.board)

    def start_game(self):
        if self.gamemode == "1":
            self.chess.board.bind("<Button-1>", self.click_handler_2_player)
        elif self.gamemode == "2":
            self.chess.board.bind("<Button-1>", self.click_handler_bot)
        else:
            print("Invalid game mode entred")
            exit(0)

    def click_handler_bot(self,event):
        if self.turn.equals(self.player1):
            posX = self.chess.size_to_x_coordinates(event.x)
            posY = self.chess.size_to_y_coordinates(event.y)
            if self.board.containsPlayerPice(posX, posY, self.turn) and not self.board.isMoveCell(posX,posY):
                self.clean_board_moves()
                self.board.actualizeMoves(posX, posY)
            elif (self.board.isMoveCell(posX,posY) and not self.board.containsPlayerPice(posX, posY, self.turn)) or (self.board.containsPlayerPice(posX, posY, self.turn) and self.board.isMoveCell(posX,posY)):
                move = self.board.board[posY][posX]['m']
                self.board.movePice(move)
                self.clean_board_moves()
                self.changeTurn()
            else:
                self.clean_board_moves()
            self.reset_board()
        if self.check_end_of_game():
            self.chess.window.destroy()
        if self.turn.equals(self.player2):
            self.chessboot.set_board(self.board)
            self.board=self.chessboot.bot_move()
            self.changeTurn()
            self.reset_board()
        if self.check_end_of_game():
            self.chess.window.destroy()
    
    def click_handler_2_player(self,event):
        posX = self.chess.size_to_x_coordinates(event.x)
        posY = self.chess.size_to_y_coordinates(event.y)
        if self.board.containsPlayerPice(posX, posY, self.turn) and not self.board.isMoveCell(posX,posY):
            self.clean_board_moves()
            self.board.actualizeMoves(posX, posY)
        elif self.board.isMoveCell(posX,posY) and not self.board.containsPlayerPice(posX, posY, self.turn):
            move = self.board.board[posY][posX]['m']
            self.board.movePice(move)
            self.clean_board_moves()
            self.changeTurn()
        elif self.board.containsPlayerPice(posX, posY, self.turn) and self.board.isMoveCell(posX,posY):
            move = self.board.board[posY][posX]['m']
            self.board.movePice(move)
            self.clean_board_moves()
            self.changeTurn()
        else:
            self.clean_board_moves()
        if self.check_end_of_game():
            self.chess.window.destroy()
        self.reset_board()

    
    def changeTurn(self):
        if self.turn.equals(self.player1):
            self.turn = self.player2
        else:
            self.turn = self.player1

    def reset_board(self):
        self.chess.create_board()
        self.chess.display_pices(self.board)

    def clean_board_moves(self):
        for row in self.board.board:
            for cell in row:
                cell['m'] = ''

    def check_end_of_game(self):
        return not self.board.check_kings_alive()