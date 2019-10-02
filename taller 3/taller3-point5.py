import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Ejemplo 1
Min        z = 2x_1 + x_2 + 3x_3
            5x_1 + 2x_2 + 7x_3 = 120 -> Restriction 1
            3x_1 + 2x_2 + 5x_3 >= 280 -> Restriction 2

Subject to:     

				Integrality
with              x_1 , x_3 >= 0
                    x_2 <=0
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 2
		[-3, -2, -5], 
		
		
		# Integrality
		[-1, 0, 0],
		[0, 1, 0],
		[0, 0, -1]

	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[280, 0, 0, 0]
)

A_eq = np.array(
	[
		
		[5, 2, 7] 

	]
)

b_eq = np.array(
	[120]
)

# Multiplicators of objective function
c = np.array(
	[2, 1, 3]
)

# Case of maximize
# c *= -1 # negate the objective coefficients

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None), method="simplex")

print("Objective = {} \n X: {}".format(res.get('fun'), res.x))

# case of maximize
#print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for i in res.keys():
	print(i, "->", res.get(i))

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, i)