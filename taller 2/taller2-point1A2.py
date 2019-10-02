import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Ejemplo 1
Maximixe        z = (540/3600)*10x_1 + (600/3600)*11x_2 + (360/3600)*13x_3

Subject to:     x_1 + x_2 + x_3 <= 94		-> Restriction 1
				(540/3600)*(360/13)x_1 +	(600/3600)*(360/13)x_2 + 
				(360/3600)*(360/13)x_3 <= 620 -> Restriction 2
				
				x_1 >= 20	-> restriction 3
				x_2 >= 20	-> restriction 4
				x_3 >= 20	-> restriction 5

				Integrality
with              x_1 , x_2, x_3 >= 0
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		
		[-3, 3, 1, 0], 

		# Restriction 1
		[1, -1, 2, 0], 
		
		
		# Restriction 3
		[-1, 0, 0, 0],

		# Restriction 4
		[0, -1, 0, 0],

		# Restriction 2
		[0, 0, -1, 0]

	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[9, 6, 0, 0, 0]
)

A_eq = np.array(
	[
		
		[0, 0, 0, 1], 

	]
)

b_eq = np.array(
	[1]
)

# Multiplicators of objective function
c = np.array(
	[-1, 1, 4, -12]
)

# Case of maximize
c *= -1 # negate the objective coefficients

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for i in res.keys():
	print(i, "->", res.get(i))

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, i)