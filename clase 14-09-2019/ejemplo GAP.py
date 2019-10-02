import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""Min z=-16x1-14x2+3*480
Ejemplo 1
Minimize        z = 3x_1 + 2x_2

Subject to:     x_1 - 2x_2 + x_3 = 5/2
				2x_1 + x_2 +x_4 = 3/2
				
				x_3 >=3
				
				x_2 >=1
				
				x_1, x_2, x_3, x_4 >= 0

				x_2 , x_3 son enteros

with              
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[0, -1, 0, 0], 
		
		# Restriction 2
		[0, 0, -1, 0],

		# inte

		[-1, 0, 0, 0], 
		
		[0, -1, 0, 0], 

		[0, 0, -1, 0], 

		[0, 0, 0, -1],

		# extra
		[0, 0, 1, 0]
	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[3, 1, 0, 0, 0, 0, 2]
)

A_eq = np.array(
	[
		# Restriction 1
		[1, -2, 1, 0], 

		[2, 1, 0, 1]
		
	]
)

b_eq = np.array(
	[5/2, 3/2]
)

# Multiplicators of objective function
c = np.array(
	[3, 2, 0, 0]
)


res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None), options={"tol":3.7e-12})

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun'), res.x)) # don't forget to retransform your objective back!

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, round(i, 4))

# for i in res.keys():
#	print(i, "->", res.get(i))