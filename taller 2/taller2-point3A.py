import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Ejemplo 1
Maximixe        z = x_1/3 + x_2/3 + x3/3 + x_4/3 + x_5/3 + x_6/3

Subject to:     x_1/8 + x_2/5 + x_3/10 <= 100	-> Restriction 1
				x_4/6 + x_5/12 + x_6/4 <= 80	-> Restriction 2

                x_1 + x_4 = x_2 + x_5		-> Restriction 3
				x_2 + x_5 = x_3 + x_6 		-> Restriction 4
				
				Integrality
with              x_1 , x_2, x_3, x_4, x_5, x_6 >= 0
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[1/8, 1/5, 1/10, 0, 0, 0], 
		
		# Restriction 2
		[0, 0, 0, 1/6, 1/12, 1/4], 
		
		# Integrality
		[-1, 0, 0, 0, 0, 0], 
		[0, -1, 0, 0, 0, 0], 
		[0, 0, -1, 0, 0, 0], 
		[0, 0, 0, -1, 0, 0], 
		[0, 0, 0, 0, -1, 0], 
		[0, 0, 0, 0, 0, -1] 
	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[100, 80, 0, 0, 0, 0, 0, 0]
)

A_eq = np.array(
	[
		# Restriction 3
		[1, -1, 0, 1, -1, 0], 
		

		# Restriction 4
		[0, 1, -1, 0, 1, -1]
	]
	
)

b_eq = np.array(
	[0, 0]
)

# Multiplicators of objective function
c = np.array(
	[1/3, 1/3, 1/3, 1/3, 1/3, 1/3]
)

# Case of maximize
c *= -1 # negate the objective coefficients

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, i)