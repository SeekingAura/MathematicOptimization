import numpy as np

"""
Max z = 16x_1 + 15x_2
40x_1 + 31x_2+x_3=124
-x_1+x_2+x_4=1
x_1+x_5=3
"""
# XB x_2, x_5. x_1
# XN x_4 x_3

# a=np.array(
# 	[
# 		[-4, 4], 
#         [4, -6], 
# 	]
# )

a=np.array(
	[
		[2, 1, 2], 
        [1, 2, 3], 
        [2, 3, 4], 
	]
)

# a=np.array(
# 	[
# 		[-2, 1, -2], 
#         [1, -2, 1], 
#         [-2, 1, -5], 
# 	]
# )
  
values, matrix = np.linalg.eig(a)
print(values)

print(np.linalg.det(a))