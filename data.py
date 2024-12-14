import csv
from typing import List

FILE_NAME = "data.csv"

def save_result(winner: str):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([winner])

def load_results() -> List[str]:
    results = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            results = [row[0] for row in reader]
    except FileNotFoundError:
        pass
    return results

