"""main program"""

from reader import Reader
from averageyear import AverageYear
from averagemonth import AverageMonth
from csvconverter import CsvConverter

csv_file = "dSST.csv"

def main():
    reader = Reader(csv_path=csv_file, csv_converter=CsvConverter)
    avg_year = AverageYear(reader)
    avg_month = AverageMonth(reader)
    avg_year.update()
    avg_month.update()
    avg_year.update()
    avg_month.update()
    avg_year.update()
    avg_month.update()
    avg_year.update()
    avg_month.update()
    avg_year.update()
    avg_month.update()


if __name__ == "__main__":
    main()

