# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# (x1-2)^4+(x1-2x2)^2
def z_function(x, y):
    return (x-2)**(4)+(x-2*y)**(2)


# x_1 -> x
# x_2 -> y

# For -2x_1 +1x_2 <= 20
## Create the vectors X and Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0, 6, 50)
y = np.linspace(-3, 4, 50)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

ax.plot_wireframe(X, Y, Z, color='green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

## Create the plot
#plt.plot(x,y,label='(x-2)^4+(x-2y)^2=0')


# Add a title
plt.title('Taller 3 punto 3a')

# Add X and y Label
#plt.xlabel('x1')
#plt.ylabel('x2')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Origin lines
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Show the plot
plt.show()