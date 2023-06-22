"""
Reader class that feeds the CSVconverter lines
"""

import linecache as lc
import time

class Reader:
    """Reader feeds the CsvConverter lines from a .csv file"""
    def __init__(self, csv_path, csv_converter):
        self.csv_path = csv_path
        self.position = 2
        self.converter = csv_converter(self.csv_path)
        self.observers = []
        
    def get_lines(self, nr=5):
        lines = [lc.getline(self.csv_path, self.position + c) for c in range(nr)]
        self.position += nr
        return self.converter.csv_to_json(lines)
    
    def add_observer(self, observer):
        """method adds observers to the subscription"""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """method removes observers from the subscription"""
        try:
            self.observers.remove(observer)
        except IndexError:
            print("observer not found")

    def notify_observers(self):
        data = 'start'
        while data:
            data = self.get_lines()
            for observer in self.observers:
                observer.update(data)
            







