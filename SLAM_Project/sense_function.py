import numpy as np
import matplotlib.pyplot as plt

#probability of the robot being in each square
p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

#color of each square in a one-dimensional world
environment = ['red', 'green', 'green', 'red', 'purple', 'green', 'purple', 'purple', 'red', 'green']
sensor = 'purple'
probability_red = 0.3
probability_green = 0.4
probability_purple = 0.3

def display_map(grid, bar_width):
    if(len(grid) > 0):
        x_labels = range(len(grid))
        plt.bar(x_labels, height=grid, width=bar_width, color='c')
        plt.xlabel('Environment Squares')
        plt.ylabel('Probability')
        plt.ylim(0, 1)
        plt.title('Probability in one-dimensional world')
        plt.xticks(np.arange(min(x_labels), max(x_labels)+1, 1))
        plt.show()

    else:
        print('Grid is empty')

def sense_function(p, sensor):
    q = []

    for i in range(len(p)):
        hit = (sensor == environment[i])
        q.append(p[i] * (hit * probability_purple + (1-hit) * (probability_green * probability_red)))

    sum_of_components = sum(q)
    for i in range(len(p)):
        q[i] = q[i]/sum_of_components
    return q

q = sense_function(p, sensor)
print(q)
display_map(q, bar_width=1)