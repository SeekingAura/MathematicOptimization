import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Ejemplo 1
Maximixe        z = -x_1 + 4x_2

Subject to:     -3x_1 + x_2 <= 6	-> Restriction 1
				x_2 >= -3	-> Restriction 2
				x_1 + 2x_2 <= 3		-> Restriction 3
				
				
with              
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[-3, 1], 
		
		# Restriction 2
		[0, -1], 

		# Restriction 3
		[1, 2]
		
		
	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[6, 3, 3]
)

A_eq = None

b_eq = None

# Multiplicators of objective function
c = np.array(
	[-1, 4]
)

# Case of maximize
c *= -1 # negate the objective coefficients

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, i)