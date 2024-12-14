class TicTacToe:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def is_valid_move(self, x: int, y: int) -> bool:
        return self.board[x][y] == ""

    def make_move(self, x: int, y: int, player: str):
        self.board[x][y] = player

    def check_winner(self) -> bool:
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
        return all(cell != "" for row in self.board for cell in row)

