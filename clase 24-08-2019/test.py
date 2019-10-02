import numpy as np

"""
Max z = 16x_1 + 15x_2
40x_1 + 31x_2+x_3=124
-x_1+x_2+x_4=1
x_1+x_5=3
"""
# XB x_2, x_5. x_1
# XN x_4 x_3
C_B=np.array(
	[
		[15,0, 16], 
	]
)

C_N=np.array(
	[
		[0,0],  
	]
)

B=np.array(
	[
		[31,0, 40], 
		[1,0, -1], 
		[0, 1, 1], 
	]
)

Binv=np.linalg.inv(B)

b=np.array(
	[
		[124], 
		[1], 
		[3], 
	]
)

N=np.array(
	[
		[0, 1], 
		[1, 0], 
		[0, 0], 
	]
)

z_0=np.matmul(np.matmul(C_B,Binv), b)

print("z_0 -> {}".format(z_0))

C_R=np.matmul(np.matmul(C_B,Binv), N)-C_N
print("C_R -> {}".format(C_R))
mResult=np.matmul(Binv,b)
print("Matrix result -> {}".format(mResult))

x_2, x_5, x_1=mResult
# print(x_2, x_5, x_1)
result=0
for i in range(len(mResult)):
	result+=mResult[i]*C_B[0][i]
print("result object".format(result))
# print("final z -> {}".format(z_0-C_R))