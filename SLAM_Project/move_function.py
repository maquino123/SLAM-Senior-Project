import numpy as np
import matplotlib.pyplot as plt

p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

#color of each square in a one-dimensional world
environment = ['red', 'green', 'green', 'red', 'purple', 'green', 'purple', 'purple', 'red', 'green']
sensor = ['purple', 'green']
probability_red = 0.3
probability_green = 0.4
probability_purple = 0.3


motion = [1,1] #robot moves to the right one square and then right again
probability_exact = 0.9
probability_over = 0.05
probability_under = 0.05

def display_map(grid, bar_width = 1):
    if(len(grid) > 0):
        x_labels = range(len(grid))
        plt.bar(x_labels, height=grid, width=bar_width, color='c')
        plt.xlabel('Environment Squares')
        plt.ylabel('Probability')
        plt.ylim(0, 1)
        plt.title('Probability in one-dimensional world')
        #plt.xticks(np.arange(min(x_labels), max(x_labels)+1, 1))
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

def move_function(p, movement):
    q = []
    for i in range(len(p)):
        index = (i - movement) % len(p)
        nextIndex = (index + 1) % len(p)
        prevIndex = (index - 1) % len(p)
        s = probability_exact * p[index]
        s = s + probability_over * p[nextIndex]
        s = s + probability_under * p[prevIndex]
        q.append(s)
    return q

for j in range(len(sensor)):
    p = sense_function(p, sensor[j])
    p = move_function(p, motion[j])

print(p)
display_map(p)