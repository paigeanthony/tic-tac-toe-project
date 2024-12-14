from tkinter import Tk
from gui import TicTacToeGUI

def main() -> None:
    """
    Initializes the main window for the Tic-Tac-Toe game and starts the GUI.
    """
    window = Tk()
    window.title("Tic-Tac-Toe Game")
    window.geometry("400x400")  # Adjust size as needed
    window.resizable(False, False)

    # Initialize and run the TicTacToe game GUI
    game_app = TicTacToeGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()
