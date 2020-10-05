from math import *
import matplotlib.pyplot as plt
import numpy as np

measurements = [2., 5., 6., 7., 10.]
motions = [1., 2., 2., 1., 1.]

measurement_sigma = 4.
motion_sigma = 2.
mu = 0.
sig = 10000.

def f(mu, sigma2, x):

    coefficient = 1.0 / sqrt(2.0 * pi * sigma2)
    exponential = exp(-0.5 * (x-mu) ** 2 / sigma2)
    return coefficient * exponential

#update function
def measurement_update(mean1, var1, mean2, var2):
    new_mean = (((var2**2) * mean1) + ((var1 ** 2)*mean2))/((var2**2) + (var1**2))
    new_var = 1/((1/(var2 ** 2)) + (1/(var1**2)))
    return [new_mean, new_var]

def prediction_function(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2

    return [new_mean, new_var]

for n in range(len(measurements)):
    mu, sig = measurement_update(mu, sig, measurements[n], measurement_sigma)
    print('Update: [{}, {}]'.format(mu, sig))

    mu, sig = prediction_function(mu, sig, motions[n], motion_sigma)
    print('Predict: [{}, {}]'.format(mu, sig))

print('\n')
print('Final result: [{}, {}]'.format(mu, sig))

mu = mu
sigma2 = sig

x_axis = np.arange(-20, 20, 0.1)

g = []
for x in x_axis:
    g.append(f(mu, sigma2, x))

plt.plot(x_axis, g)
plt.show()