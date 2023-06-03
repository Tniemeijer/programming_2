import matplotlib.pyplot as plt

class DataPlot:

    def plot(data, period='month'):
        #lets try it for the month of may
        match period:
            case 'month':
                x = [float(year) for year in list(data.keys())]
            case _:
                x = [int(year) for year in list(data.keys())]
        labels = [i for i in range(round(min(x)),round(max(x)),2)]
        y = [per for per in data.values()]
        plt.scatter(x=x,y=y)
        plt.xticks(labels,labels,rotation='vertical')
        plt.title(f'Temperature anomaly / {period}')
        plt.show()