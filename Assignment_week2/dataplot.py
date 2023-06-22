import matplotlib.pyplot as plt
import numpy as np

class DataPlot:

    def plot(data, period='month'):
        match period:
            case 'month':
                x = [float(year) for year in list(data.keys())]
            case _:
                x = [int(year) for year in list(data.keys())]
        labels = [i for i in range(round(min(x)),round(max(x)),5)]
        y = [per for per in data.values()]
        plt.scatter(x=x,y=y)
        plt.xticks(labels,labels,rotation='vertical')
        plt.yticks(np.arange(-1,2,.25))
        plt.title(f'Temperature anomaly / {period}')
        plt.show(block=False)
        plt.pause(.5)
        plt.close()