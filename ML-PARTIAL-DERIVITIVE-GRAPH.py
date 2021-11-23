import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x**2  + y**2 - 2*x - 6*y + 20
x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'viridis')
plt.show()