import matplotlib.pyplot as plt


class Plotter:

    def sensor_plot(self, data, sensor):
        sensor = f'sensor_{sensor}'
        broken = data[data["machine_status"] == 'BROKEN']
        recovery = data[data["machine_status"] == 'RECOVERING']
        anomaly = data[data['pred'] == -1]
        fig, ax = plt.subplots(figsize=(25,5))
        ax.plot(data[sensor], color='grey')
        ax.plot(recovery[sensor], linestyle='none', color='orange', marker='o', markersize=5)
        ax.plot(broken[sensor], linestyle='none', marker='X', color='red', markersize=25)
        ax.plot(anomaly[sensor], linestyle='none', marker = 'X', color = 'blue')
        ax.set_title(sensor)
        plt.close()
        return fig