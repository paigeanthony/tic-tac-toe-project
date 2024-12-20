import unittest
from logic import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """
    Unit tests for the TicTacToe game logic.
    """

    def setUp(self) -> None:
        """
        Sets up a new game instance before each test.
        """
        self.game = TicTacToe()

    def test_make_valid_move(self) -> None:
        """
        Tests making a valid move and checking if the board updates correctly.
        """
        self.game.make_move(0, 0, "X")
        self.assertEqual(self.game.board[0][0], "X")

    def test_check_winner(self) -> None:
        """
        Tests checking if the game correctly detects a winner.
        """
        self.game.make_move(0, 0, "X")
        self.game.make_move(0, 1, "X")
        self.game.make_move(0, 2, "X")
        self.assertTrue(self.game.check_winner())

    def test_is_draw(self) -> None:
        """
        Tests checking if the game correctly detects a draw.
        """
        self.game.reset_board()
        moves = [
            (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
            (1, 0, "O"), (1, 1, "X"), (1, 2, "O"),
            (2, 0, "X"), (2, 1, "O"), (2, 2, "X")
        ]
        for move in moves:
            self.game.make_move(move[0], move[1], move[2])
        self.assertTrue(self.game.is_draw())

if __name__ == "__main__":
    unittest.main()
