import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#plt.style.use('_mpl-gallery')
# make data
'''
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
'''
# 2
# Dataset generatio
'''
a, b, c = 10., 28., 8. / 3. # BROKEN SOMEWHERE
def lorenz_map(X, dt = 1e-2):
        X_dt = np.array([a * (X[1] - X[0]),
        X[0] * (b - X[2]) - X[1],
        X[0] * X[1] - c * X[2]])
        return X + dt * X_dt
points = np.zeros((2000, 3))
X = np.array([.1, .0, .0])
for i in range(points.shape[0]):
       points[i], X = X, lorenz_map(X)
# Plotting
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b,c))
ax.scatter(points[:, 0], points[:, 1], points[:, 2], zdir = 'y',c = 'k')
plt.show()
'''
# 3 # GOD THIS IS COOL
'''
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
X, Y = np.meshgrid(x, y)
Z = np.sinc(np.sqrt(X ** 2 + Y ** 2))
fig = plt.figure()
ax = fig.gca(projection = '3d') # DUNNO HOW TO FIX THIS ERROR seems to want me to get rid of it
ax.plot_surface(X, Y, Z, cmap=cm.gray)
plt.show()
'''
# 4
'''
# Generate torus mesh
angle = np.linspace(0, 2 * np.pi, 32)
theta, phi = np.meshgrid(angle, angle)
r, R = .25, 1.
X = (R + r * np.cos(phi)) * np.cos(theta)
Y = (R + r * np.cos(phi)) * np.sin(theta)
Z = r * np.sin(phi)
# Display the mesh
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.plot_surface(X, Y, Z, color = 'w', rstride = 1, cstride = 1)
plt.show()
'''
# 5 Wave Functions?
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X ** 2 + Y ** 2))
u = np.exp(-(x ** 2))
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_zlim3d(0, 3)
ax.plot(x, u, zs=3, zdir='y', lw = 2, color = '.75')
ax.plot(x, u, zs=-3, zdir='x', lw = 2., color = 'k')
ax.plot_surface(X, Y, Z, color = 'w')
plt.show()
# 6 # UI

# 7

# 8

# 9

# 10

# 11

# 13

# 14

# 15