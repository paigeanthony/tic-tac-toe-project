class TicTacToe:
    """
    This class implements the game logic for Tic-Tac-Toe.
    It manages the game board, checks for valid moves, and determines the winner.
    """

    def __init__(self) -> None:
        """
        Initializes a new game of Tic-Tac-Toe by resetting the game board.
        """
        self.reset_board()

    def reset_board(self) -> None:
        """
        Resets the game board to an empty state (3x3 grid).
        """
        self.board: list[list[str]] = [["" for _ in range(3)] for _ in range(3)]

    def is_valid_move(self, x: int, y: int) -> bool:
        """
        Checks whether the move at position (x, y) is valid (i.e., the cell is empty).

        Args:
            x (int): The row index.
            y (int): The column index.

        Returns:
            bool: True if the move is valid, otherwise False.
        """
        return self.board[x][y] == ""

    def make_move(self, x: int, y: int, player: str) -> None:
        """
        Makes a move for the current player at the specified position.

        Args:
            x (int): The row index.
            y (int): The column index.
            player (str): The player making the move ("X" or "O").
        """
        self.board[x][y] = player

    def check_winner(self) -> bool:
        """
        Checks whether there is a winner (three in a row, column, or diagonal).

        Returns:
            bool: True if there is a winner, otherwise False.
        """
        # Check rows, columns, diagonals
        for i in range(3):
            if all(self.board[i][j] == self.board[i][0] and self.board[i][0] != "" for j in range(3)):
                return True
            if all(self.board[j][i] == self.board[0][i] and self.board[0][i] != "" for j in range(3)):
                return True

        if all(self.board[i][i] == self.board[0][0] and self.board[0][0] != "" for i in range(3)):
            return True
        if all(self.board[i][2-i] == self.board[0][2] and self.board[0][2] != "" for i in range(3)):
            return True
        return False

    def is_draw(self) -> bool:
        """
        Checks whether the game is a draw (i.e., the board is full and no one has won).

        Returns:
            bool: True if the game is a draw, otherwise False.
        """
        return all(cell != "" for row in self.board for cell in row)
