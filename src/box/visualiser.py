import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

from .sensor import Header, Data

class SplitAnimator:
    ANIMATION_SPEED = 0.01

    def __init__(self, fig, ax, sensors):
        self.fig = fig
        self.ax = ax
        self.sensors = sensors

        # Index of the sensor being drawn
        self.sensor_index = 0
        self.end_sensor_index = len(sensors)

        # Static (completed) path
        self.static_path = ([sensors[0].position[0]], [sensors[0].position[1]])

        # Positions for the animated path
        self.previous_sensor_position = sensors[0].position
        self.current_position = self.previous_sensor_position
        self.next_sensor_position = sensors[self.sensor_index].position

        # Animated path between sensors
        self.animated_path = ([self.previous_sensor_position[0], self.next_sensor_position[0]],
                              [self.previous_sensor_position[1], self.next_sensor_position[1]])

        # Percentage between previous and next sensor
        self.split_percentage = 0

        self.counter = count(0, 1)
        self.animation = FuncAnimation(fig=self.fig, func=self.update, interval=1)

    def update(self, i):
        idx = next(self.counter)
        self.split_percentage += self.ANIMATION_SPEED

        self.current_position = self.lerp(self.previous_sensor_position,
                                          self.next_sensor_position,
                                          self.split_percentage)

        self.animated_path[0][-1] = self.current_position[0]
        self.animated_path[1][-1] = self.current_position[1]

        # Plot the static path
        # self.ax.plot(self.static_path[0], self.static_path[1], 'g', linewidth=2.0)

        # Draw the animated path
        self.ax.plot(self.animated_path[0], self.animated_path[1], 'g', linewidth=2.0)

        # If the split is complete
        if (1 <= self.split_percentage):
            self.split_percentage = 0

            # Go to the next sensor
            self.sensor_index += 1
            self.sensor_index %= self.end_sensor_index

            # If the next sensor is the start, clear the static path
            if (0 == self.sensor_index):
                self.static_path[0].clear()
                self.static_path[1].clear()

            # Update the next sensor position
            self.previous_sensor_position = self.next_sensor_position
            self.next_sensor_position = self.sensors[self.sensor_index].position

            # Add the new end point to the static path
            self.static_path[0].append(self.sensors[self.sensor_index].position[0])
            self.static_path[1].append(self.sensors[self.sensor_index].position[1])

            # Move the start of the animated path to the current position
            self.animated_path[0][0] = self.current_position[0]
            self.animated_path[1][0] = self.current_position[1]

    def lerp(self, a : tuple, b : tuple, c : float):
        return (a[0] + (b[0] - a[0]) * c,
                a[1] + (b[1] - a[1]) * c)

class Visualiser:
    def __init__(self, header : Header, data : Data):
        # Setup plot
        self.fig, self.ax = plt.subplots()
        self.data = data

        sensor_positions = [[], []]

        # Unpack the data
        for sensor in self.data.sensor_data:
            sensor_positions[0].append(sensor.position[0])
            sensor_positions[1].append(sensor.position[1])

        self.sensor_positions = (np.array(sensor_positions[0]),
                                 np.array(sensor_positions[1]))

        self.animation = None
    
    def plot_points(self, options : str = ''):
        self.ax.plot(self.sensor_positions[0],
                     self.sensor_positions[1],
                     options)

    def plot_lines_animated(self):
        # total_sensors = len(self.sensor_positions[0])

        # split_index = 0
        # sensor_index = split_index % total_sensors
        
        # # Previous and next sensor
        # previous_position = self.data.sensor_data[sensor_index].position
        # next_position = self.data.sensor_data[(sensor_index + 1) % total_sensors].position

        # # Linear interpolation for 2D tuples
        # def lerp(a : tuple, b : tuple, c : float):
        #     return (a[0] + (b[0] - a[0]) * c,
        #             a[1] + (b[1] - a[1]) * c)

        # # Percentage between previous and next sensors
        # split_percentage = 0

        # # Current position between previous and next sensors
        # current_position = lerp(previous_position, next_position, split_percentage)

        # # Start with points at the first sensor position
        # completed_x = [previous_position[0]]
        # completed_y = [previous_position[1]]

        # animated_x = [previous_position[0], current_position[0]]
        # animated_y = [previous_position[1], current_position[1]]

        # self.ax.plot(completed_x, completed_y, 'g', linewidth=2.0)
        # self.ax.plot(animated_x, animated_y, 'g', linewidth=2.0)

        # counter = count(0, 1)
        # def update(i):
        #     count = next(counter)

        #     split_percentage += 0.01

        #     # Update end of animated line
        #     current_position = lerp(previous_position, next_position, split_percentage)

        #     animated_x[-1] = current_position[0]
        #     animated_y[-1] = current_position[1]

        #     # Split is completed
        #     if (split_percentage >= 1):
        #         split_percentage = 0

        #         # Go to the next sensor
        #         split_index += 1
        #         sensor_index = split_index % total_sensors
                
        #         # Clear the path when the index goes back to the start
        #         if (0 == sensor_index):
        #             completed_x.clear()
        #             completed_y.clear()

        #         # Add latest sensor to the completed path
        #         completed_x.append(self.sensor_positions[0][sensor_index % total_sensors])
        #         completed_y.append(self.sensor_positions[1][sensor_index % total_sensors])

        #         # Go to next previous and next positions
        #         previous_position = next_position
        #         next_position = self.data.sensor_data[(sensor_index + 1) % total_sensors].position

        # self.animation = FuncAnimation(fig=self.fig, func=update, interval=200)
        self.animator = SplitAnimator(self.fig, self.ax, self.data.sensor_data)

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