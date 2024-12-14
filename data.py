import csv
from typing import List

FILE_NAME = "data.csv"

def save_result(winner: str):
    """
    Saves the result of the game (winner or draw) to a CSV file.

    Args:
        winner (str): The winner of the game ("X", "O", or "Draw").
    """
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([winner])

def load_results() -> List[str]:
    """
    Loads the results from the CSV file and returns them as a list of strings.

    Returns:
        List[str]: A list of game results.
    """
    results = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            results = [row[0] for row in reader]
    except FileNotFoundError:
        pass
    return results
