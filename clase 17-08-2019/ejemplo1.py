import numpy as np
from scipy.optimize import linprog

# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method
# https://stackoverflow.com/questions/44429356/simplex-algorithm-in-scipy-package-python
"""
Ejemplo 1
Maximixe          z = 3*x1 + 4*x2
Subject to:       1*x1 + 2*x2 <= 6
				  2*x1 + 2*x2 <= 8

with              x1 >= 0, x2 >= 0
"""
A = np.array(
	[
		[1, 2], 
		[2,2], 
		[-1, 0], 
		[0, -1]
	]
)
b = np.array(
	[6, 8, 0, 0]
)
c = np.array(
	[3,4]
)

# max
c *= -1 # negate the objective coefficients

res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

# print('Optimal value:', res.fun, '\nX:', res.x)

# max
print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!