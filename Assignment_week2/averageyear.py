"""
Class that stores average temperature data of the year.
"""
import numpy as np
from dataplot import DataPlot

class AverageYear:
    """average yearly temparature anomaly class"""
    def __init__(self):
        self.avg_year = {}
        self.plot = DataPlot
    
    def get_data(self, data):
        lines = data
        self.avg_year.update({
                list(i.values())[0]:np.mean(
                  [float(v) for v in list(i.values())[1:13]]) 
                  for i in lines if list(i.values()) != ""
                })
    def update(self, data):
        self.get_data(data)
        self.plot.plot(self.avg_year,period='year')

