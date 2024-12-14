from tkinter import Frame, Button, Label, StringVar, messagebox
from logic import TicTacToe
from data import save_result, load_results

class TicTacToeGUI:
    def __init__(self, window):
        self.window = window
        self.game = TicTacToe()
        self.buttons = []
        self.current_player = StringVar(value="X")
        self.setup_gui()

    def setup_gui(self):
        self.label = Label(self.window, text="Tic-Tac-Toe: Player X's Turn")
        self.label.pack()

        # Board setup
        board_frame = Frame(self.window)
        board_frame.pack()

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = Button(
                    board_frame, text="", height=3, width=6,
                    command=lambda x=i, y=j: self.make_move(x, y)
                )
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, x, y):
        if not self.game.is_valid_move(x, y):
            return
        current_player = self.current_player.get()
        self.game.make_move(x, y, current_player)
        self.buttons[x][y].config(text=current_player)

        if self.game.check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Wins!")
            save_result(current_player)
            self.reset_game()
        elif self.game.is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            save_result("Draw")
            self.reset_game()
        else:
            self.current_player.set("O" if current_player == "X" else "X")
            self.label.config(text=f"Player {self.current_player.get()}'s Turn")

    def reset_game(self):
        self.game.reset_board()
        self.current_player.set("X")
        self.label.config(text="Tic-Tac-Toe: Player X's Turn")
        for row in self.buttons:
            for button in row:
                button.config(text="")

