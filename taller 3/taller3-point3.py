# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
# x_1 -> x
# x_2 -> y

# For -2x_1 +1x_2 <= 20
## Create the vectors X and Y
x = np.array(range(-25, 25))
y = 20 + 2*x

## Create the plot
plt.plot(x,y,label='y = 20+2x')

# For 1x_1 + 2x_2 <= 15
## Create the vectors X and Y
x = np.array(range(-25, 25))
y = 15/2 - x/2

## Create the plot
plt.plot(x,y,label='y = 15/2-x/2')

# For x_2 >= -2
## Create the vectors X and Y
x = np.array(range(-25, 25))
y = -2 + x*0

## Create the plot
plt.plot(x,y,label='y = -2')

# Get intersecctions with restriction 1 and 2
# 1 -> y = 20+2x    -> -2x+ y=20
# 2 -> y = 15/2-x/2 ->   x+2y=15
a = np.array([[-2,1], [1,2]])
b = np.array([20,15])
x = np.linalg.solve(a, b)
ecuationsLabel="y = 20+2x ∩ y = 15/2-x/2"
plt.scatter(x[0], x[1], c="black", label=ecuationsLabel+"\n"+str("("+str(x[0])
    +","+str(x[1])+")").center(len(ecuationsLabel), " ")
)

# Get intersecctions with restriction 1 and 3
# 1 -> y = 20+2x    -> -2x+y=20
# 3 -> y = -2       ->  0x+y=-2
a = np.array([[-2,1], [0,1]])
b = np.array([20,-2])
x = np.linalg.solve(a, b)
ecuationsLabel="y = 20+2x ∩ y = -2"
plt.scatter(x[0], x[1], c="red", label=ecuationsLabel+"\n"+str("("+str(x[0])
    +","+str(x[1])+")").center(len(ecuationsLabel), " ")
)

# Get intersecctions with restriction 2 and x
# 2 -> y = 15/2-x/2 ->   x+2y=15
# x -> x = 0        ->   x+0y=0
a = np.array([[1,2], [1,0]])
b = np.array([15,0])
x = np.linalg.solve(a, b)
ecuationsLabel="y = 15/2-x/2 ∩ x = 0"
plt.scatter(x[0], x[1], c="blue", label=ecuationsLabel+"\n"+str("("+str(x[0])
    +","+str(x[1])+")").center(len(ecuationsLabel), " ")
)

# Add a title
plt.title('Taller 3 punto 3a')

# Add X and y Label
plt.xlabel('x1')
plt.ylabel('x2')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Origin lines
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Show the plot
plt.show()