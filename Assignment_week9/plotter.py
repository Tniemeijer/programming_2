import matplotlib.pyplot as plt


class Plotter:
    """
    Plot creating class
    """
    def __init__(self, sensors):
        """
        Initializes the plotter

        --------------
        params: 
                sensors (list): list with sensors used for plotting
        """
        self.sensors = sensors
        
    def sensor_plot(self, data):
        """
        plotting function

        --------------
        params:
                data (pandas.Dataframe): dataframe with the sensor data and
                                        predictions.
        
        output: 
                plot (mpl.pyplot.subplots): closed plot with sensor and
                                             prediction data.
        """
        num_plots = len(self.sensors)
        fig, axes = plt.subplots(num_plots,figsize=(25,5*num_plots))
        plt.tight_layout()
        for ax, sensor in zip(axes.flat,self.sensors):
            sensor_name = f'sensor_{sensor}'
            broken = data[data["machine_status"] == 'BROKEN']
            recovery = data[data["machine_status"] == 'RECOVERING']
            anomaly = data[data['pred'] == -1]
            ax.plot(data[sensor_name], color='grey', label='sensor data')
            ax.plot(recovery[sensor_name], linestyle='none', color='orange',
                            marker='o', markersize=5, label='Recovery')
            ax.plot(broken[sensor_name], linestyle='none', marker='X',
                        color='red', markersize=25, label='Broken')
            ax.plot(anomaly[sensor_name], linestyle='none', marker = 'X',
                                color = 'blue', label='Prediction')
            ax.legend()
            ax.set_title(sensor_name)
        plt.close()
        return fig