import numpy as np
import numpy.matlib

a=np.arange(12).reshape(3,4)
print('矩阵\n{}\n转置后为\n{}\n'.format(a,a.T))
print(np.empty((3,2)))
print(np.zeros((2,1)))
print(np.ones((4,2)))
print(np.matlib.eye(n=4,M=2,k=0,dtype=float))
print(np.matlib.identity(5,dtype=int))
print(np.matlib.rand((5,3)))