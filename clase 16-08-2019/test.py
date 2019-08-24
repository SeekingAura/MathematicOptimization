import numpy as np
from scipy.optimize import linprog

# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method
"""
Minimize          w = 10*y1 + 15*y2 + 25*y3
Subject to:       y1 + y2 + y3 >= 1000
                  y1 - 2*y2    >= 0
                            y3 >= 340
with              y1 >= 0, y2 >= 0
"""
A = np.array(
    [
        [-1, -1, -1], 
        [-1,2, 0], 
        [0, 0, -1], 
        [-1, 0, 0], 
        [0, -1, 0]
    ]
)
b = np.array(
    [-1000, 0, -340, 0, 0]
)
c = np.array(
    [10,15,25]
)

res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal value:', res.fun, '\nX:', res.x)