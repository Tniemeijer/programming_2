"""Class that creates an average month report over the last five years"""

from dataplot import DataPlot

class AverageMonth:
    """Average month class"""
    def __init__(self, reader):
        self.reader = reader
        self.anomal_month = {}
        self.plot = DataPlot

    def get_data(self):
        lines = self.reader.get_lines()
        months = [month for line in lines for month in list(line.keys())[1:13]]
        for i in lines:
            if list(i.values()) != "":
                self.anomal_month.update({f'{list(i.values())[0]}.{round(c/12 * 1e6) if c !=0 else 0}':float(v) 
                                  for c,v in enumerate(list(i.values())[1:13])})
                
    def update(self):
        self.get_data()
        self.plot.plot(self.anomal_month)
    



