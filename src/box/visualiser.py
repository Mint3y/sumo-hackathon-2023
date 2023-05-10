import numpy as np
import matplotlib.pyplot as plt

from .sensor import Header, Data

class Visualiser:
    def __init__(self, header : Header, data : Data):
        # Setup plot
        self.fig, self.ax = plt.subplots()

        sensor_positions = [[], []]

        # Unpack the data
        for sensor in data.sensor_data:
            sensor_positions[0].append(sensor.position[0])
            sensor_positions[1].append(sensor.position[1])

        self.sensor_positions = (np.array(sensor_positions[0]),
                                 np.array(sensor_positions[1]))
    
    def plot_points(self, options : str = ''):
        self.ax.plot(self.sensor_positions[0],
                     self.sensor_positions[1],
                     options)

    def plot_lines(self, options : str = ''):
        self.ax.plot(self.sensor_positions[0],
                     self.sensor_positions[1],
                     options,
                     linewidth=2.0)

    def plot_labels(self):
        end = len(self.sensor_positions[0])

        for i in range(end):
            x = self.sensor_positions[0][i]
            y = self.sensor_positions[1][i]
            text = "(" + str(x) + ", " + str(y) + ")"
            self.ax.text(x, y, text, size=12)

    def show(self):
        plt.show()