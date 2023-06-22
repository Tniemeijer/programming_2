import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, data):
        self.data = data

    def sensor_plot(self, sensor):
        sensor_data = self.data[sensor]
        broken = sensor_data[sensor_data["machine_status"] == 'BROKEN']
        recovery = sensor_data[sensor_data["machine_status"] == 'RECOVERING']
        anomaly = sensor_data[sensor_data['pred'] == -1]
        fig, ax = plt.subplots(figsize=(25,5))
        ax.plot(sensor_data[sensor], color='grey')
        ax.plot(recovery[sensor], linestyle='none', color='orange', marker='o', markersize=5)
        ax.plot(broken[sensor], linestyle='none', marker='X', color='red', markersize=25)
        ax.plot(anomaly[sensor], linestyle='none', marker = 'X', color = 'blue')
        ax.set_title(sensor)
        plt.close()
        return fig