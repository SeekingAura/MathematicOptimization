import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Ejemplo 1
Maximixe		z = x_1 + 10x_2

Subject to:	 x_1 + 1x_2 <= 5		-> Restriction 1
				x_1 + 2x_2 <= 9		-> Restriction 2
				x_1 + 3x_2 <= 15	-> Restriction 3
				x_1 + 4x_2 <= 19	-> Restriction 4
				x_1 + 5x_2 <= 21	-> Restriction 5
				x_1 + 6x_2 <= 24	-> Restriction 6
				x_1 + 7x_2 <= 26	-> Restriction 7
				x_1 + 8x_2 <= 30	-> Restriction 8
				x_1 + 9x_2 <= 31	-> Restriction 9
				x_1 + 10x_2 <= 35   -> Restriction 10
				
				
with			  
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[1, 1], 
		
		# Restriction 2
		[1, 2], 

		# Restriction 3
		[1, 3], 

		# Restriction 4
		[1, 4], 

		# Restriction 5
		[1, 5], 

		# Restriction 6
		[1, 6], 

		# Restriction 7
		[1, 7], 

		# Restriction 8
		[1, 8], 

		# Restriction 9
		[1, 9], 

		# Restriction 10
		[1, 10], 
		
	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[5, 9, 15, 19, 21, 24, 26, 30, 31, 35]
)

A_eq = None

b_eq = None

# Multiplicators of objective function
c = np.array(
	[1, 10]
)

# Case of maximize
c *= -1 # negate the objective coefficients

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for varName, i in zip(["x_1", "x_2"], res.x):
	print(varName, i)