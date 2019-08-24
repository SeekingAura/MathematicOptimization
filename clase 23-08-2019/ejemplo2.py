import numpy as np
from scipy.optimize import linprog

# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method
"""
Ejemplo 1
Maximixe        z = x1*0.12 + x2*0.16 + x3*0.16 
                    + x4*0.14
Subject to:     x1 + x2 + x3 + x4 <= 1
				x1 >= 0.55 * (x1+x2)
                x1 >= 0.25 * (x1+x2+x3+x4)
                x2 >= 0.30 * (x1+x2+x3+x4)
                z  <= 0.14 * (x1+x2+x3+x4)

                0<=xi<=1 i=1 ... 4

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