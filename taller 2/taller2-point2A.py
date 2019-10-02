import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Ejemplo 1
Maximixe        z = 8x_1 +12x_2

Subject to:     20x_1 + 60x_2 <= 60000	-> Restriccion 1
				70x_1 + 60x_2 <= 84000	-> Restricción 2
				12x_1 +4x_2 <= 12000	-> Restricción 3    

				
				Integrality
with              x_1 , x_2 >= 0
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[20, 60], 
		
		# Restriction 2
		[70, 60], 
		
		# Restriction 3
		[12, 4], 

		# Integrality
		[-1, 0], 
		[0, -1]
	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[60000, 84000, 12000, 0, 0]
)

A_eq = None

b_eq = None

# Multiplicators of objective function
c = np.array(
	[8, 12]
)

# Case of maximize
c *= -1 # negate the objective coefficients
# for solve simplex must be increase tolerance
res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None), options={"tol":3.7e-12})

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for varName, i in zip(["x_1", "x_2", "x_3", "x_4", "x_5", "x_6"], res.x):
	print(varName, i)