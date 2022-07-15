
# https://stackoverflow.com/questions/56380536/hilbert-transform-in-python

import math
from scipy.fftpack import * # hilbert
import numpy as np
import matplotlib.pyplot as plt

def hilbert_from_scratch(u):
    # N : fft length
    # M : number of element to zero out
    # U : DFT of u
    # v : IDFT of H(u)

    N = len(u)

    # take forwart Fourier transform
    U = np.fft.fft(u)
    M = N - N//2 - 1

    # zero out negative frequency components
    U[N//2+1:] = [0] * M

    # double fft energy except @ DC0
    U[1:N//2] = 2 * U[1:N//2]
    
    # take inverse Fourier transform
    v = np.fft.ifft(U)
    return v

if __name__ == '__main__':
    N = 32
    f = 1
    dt = 1.0 / N
    y = []
    for n in range(N):
        x = 2*math.pi*f*dt*n
        y.append(math.sin(x))
    z1 = hilbert_from_scratch(y)
    z2 = hilbert(y)
    print(" n     y fromscratch scipy")
    for n in range(N):
        print('{:2d} {:+5.2f} {:+10.2f} {:+5.2f}'.format(n, y[n], z1[n], z2[n]))
    plt.plot(z1.real, z1.imag, '-.r*')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()
    
# Essai 2
    
fig = plt.figure()
ax = plt.axes(projection='3d')

def f(x):
    return x**2 + 1 

a = np.arange(-10,10,1)
b = np.arange(-10,10,1)
carray = np.zeros((len(a), len(b)), dtype=complex)

for i in range(-10,10,1):
    for j in range(-10,10,1):
        carray[i, j] = complex(i, j)

carray = f(carray)  #<-- use f()

ax.contour3D(a, b, carray)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# Essai 3

## https://matplotlib.org/stable/gallery/mplot3d/lines3d.html
    
ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()

# Essai 4

## https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
plt.show()
