import numpy as np
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

"""Min z=-16x1-14x2+3*480
Ejemplo 1
Minimize        z = -16x_1 - 14x_2 + 'x_3'3*480

Subject to:     7x_1 + 3x_2 <= 480-(480*0.12)	-> Restriction 1
				5x_1 + 5x_2 <= 480-(480*0.14)	-> Restriction 2
				4x_1 + 6x_2 <= 480-(480*0.13)	-> Restriction 3
				
                x_3 = 1     -> Extra restriction 1
				x_1, x_2 >= 0 -> Integrality
with              
"""

# Restrictions part left of '<='
A_ub = np.array(
	[
		# Restriction 1
		[7, 3, 0], 
		
		# Restriction 2
		[5, 5, 0], 

		# Restriction 3
		[4, 6, 0],

        # Integrality
        [-1, 0, 0],
        [0, -1, 0]
		
	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[480-(480*0.12), 480-(480*0.14), 480-(480*0.13), 0, 0]
)

A_eq = np.array(
	[
		# Restriction 1
		[0, 0, 1], 
		
	]
)

b_eq = np.array(
	[1]
)

# Multiplicators of objective function
c = np.array(
	[-16, -14, 3*480]
)


res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None))

# print('Optimal value:', res.fun, '\nX:', res.x)

# case of maximize
print("Objective = {} \n X: {}".format(res.get('fun'), res.x)) # don't forget to retransform your objective back!

for varName, i in zip(["x_"+str(x) for x in range(1, len(res.x)+1)], res.x):
	print(varName, i)