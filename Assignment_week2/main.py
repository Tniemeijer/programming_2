"""main program"""

from reader import Reader
from averageyear import AverageYear
from averagemonth import AverageMonth
from csvconverter import CsvConverter

csv_file = "dSST.csv"

def main():
    prod = Reader(csv_path=csv_file, csv_converter=CsvConverter)
    cons1 = AverageYear()
    cons2 = AverageMonth()
    prod.add_observer(cons1)
    prod.add_observer(cons2)
    prod.notify_observers()


if __name__ == "__main__":
    main()

