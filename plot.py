from matplotlib import pyplot as plt
import numpy as np
from math import *

# test functions
def f(x):
    return x*x/10

def g(x):
    return -x**2/10

def h(x):
    return -x/3

# define 100 values between -pi and pi
X = np.linspace(-np.pi, np.pi, 100) 
Y = np.sin(X)
Z = np.cos(X)
W = g(X)

# plot
plt.plot(X, Y, color = "blue", linewidth = 1.5, linestyle = "-")
plt.plot(X, Z, color = "red", linewidth = 3)
plt.plot(X, [f(x) for x in X], color = "orange", linewidth = 5)
plt.plot(X, W, linewidth = 3) # autodefined color (will be different from previous ones)
plt.plot(X, h(X), color = "green", linewidth = 3)

# mage is closed and freed from memory after show() method.
plt.savefig("graph")
plt.show()
