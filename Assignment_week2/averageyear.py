"""
Class that stores average temperature data of the year.
"""
from dataplot import DataPlot

class AverageYear:
    """average yearly temparature anomaly class"""
    def __init__(self, reader):
        self.reader = reader
        self.avg_year = {}
        self.plot = DataPlot
    
    def get_data(self):
        lines = self.reader.get_lines()
        self.avg_year.update({
                list(i.values())[0]:sum(
                  [float(v) for v in list(i.values())[1:13]]) 
                  for i in lines if list(i.values()) != ""
                })
    def update(self):
        self.get_data()
        self.plot.plot(self.avg_year,period='year')

