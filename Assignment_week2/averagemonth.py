"""Class that creates an average month report over the last five years"""

from dataplot import DataPlot

class AverageMonth:
    """Average month class"""
    def __init__(self):
        self.anomal_month = {}
        self.plot = DataPlot

    def get_data(self, data):
        lines = data
        for i in lines:
            if list(i.values()) != "":
                self.anomal_month.update({f'{list(i.values())[0]}.{round(c/12 * 1e6) if c !=0 else 0}':float(v) 
                                  for c,v in enumerate(list(i.values())[1:13])})
                
    def update(self, data):
        self.get_data(data)
        self.plot.plot(self.anomal_month)
        
    



