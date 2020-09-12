import numpy as np
import matplotlib.pyplot as plt

p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

def display_map(grid, bar_width):
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
#display_map(p)

def initialize_robot(grid_length):
    p = []

    for i in range(grid_length):
        p.append(1.0/grid_length)
    return p

p = initialize_robot(10)
print(p)
display_map(p, bar_width=0.9)