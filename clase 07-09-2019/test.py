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
B = np.array(
	[
		# Restriction 1
		[1], 

		# Restriction 2
		[3],
		

	]
)

# Resticctions part rigth of '<='
b_ub = np.array(
	[-8, -6, 0, 0, 0]
)
