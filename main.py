from tkinter import Tk
from gui import TicTacToeGUI

def main():
    window = Tk()
    window.title("Tic-Tac-Toe Game")
    window.geometry("400x400")
    window.resizable(False, False)

    game_app = TicTacToeGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()

