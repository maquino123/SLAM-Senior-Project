from math import *
import matplotlib.pyplot as plt
import numpy as np

def f(mu, sigma2, x):

    coefficient = 1.0 / sqrt(2.0 * pi * sigma2)
    exponential = exp(-0.5 * (x-mu) ** 2 / sigma2)
    return coefficient * exponential

mu = 10
sigma2 = 4

x_axis = np.arange(0, 20, 0.1)

g = []

for x in x_axis:
    g.append(f(mu, sigma2, x))

plt.plot(x_axis, g)
plt.show()

gauss_1 = f(19, 4, 8)
print(gauss_1)
