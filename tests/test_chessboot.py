import unittest
from Board import Board
from ChessBot import ChessBot
class TestChessBot(unittest.TestCase):


    def setUp(self):
        self.board=Board()
        self.chessbot=ChessBot(self.board)


    def test_all_pices_evaluation(self):
        self.assertEqual(0, self.chessbot.evaluation(self.board))
        


if __name__ == '__main__':
    unittest.main()