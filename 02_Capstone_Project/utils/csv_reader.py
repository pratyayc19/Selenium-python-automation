import csv
from pathlib import Path


class CSVReader:

    @staticmethod
    def read_test_data():
        csv_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "test_data.csv"
        )

        with open(csv_path, mode="r", encoding="utf-8") as file:
            return list(csv.DictReader(file))