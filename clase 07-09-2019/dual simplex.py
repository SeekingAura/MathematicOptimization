# https://stackoverflow.com/questions/50374255/efficiently-get-shadow-prices-in-scipy-linprog
import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""
Min        z = 2x_1 + 3x_2 + 2x_3

Subject to:     
				x_1 + 4x_2 + 2x_3 >= 8 -> Restriction 1
				3x_1 + 2x_2 + 2x_3 >= 6 -> Restriction 2

				Integrality
with              x_1 , x_2, x_3 >= 0
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[-1, -4, -2], 

		# Restriction 2
		[-3, -2, -2],
		

	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[-8, -6]
)

A_eq = None

b_eq = None

# Multiplicators of objective function
c = np.array(
	[2, 3, 2]
)

# Case of maximize
# c *= -1 # negate the objective coefficients

# Dual
dual_c = b_ub
dual_b = 1.0 * c
dual_A = -1.0 * np.transpose(A_ub)

x1_bnds =(0, None) # bounds on x1
x2_bnds = (0,None) # bounds on x2

# Normal
# res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

# Dual ¿?
res = linprog(c=dual_c, A_ub=dual_A, b_ub=dual_b, A_eq=A_eq, b_eq=b_eq, bounds=(x1_bnds, x2_bnds))
print('Optimal value:', res.fun, '\nX:', res.x)




# case of maximize
# print("Objective = {} \n X: {}".format(res.get('fun') * -1, res.x)) # don't forget to retransform your objective back!

for i in res.keys():
	print(i, "->", res.get(i))

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, i)