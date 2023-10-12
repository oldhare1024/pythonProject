import numpy as np

A=np.array([[1,0,1,-1],
           [2,2,0,2]])
B=np.array([[4,1,0],
            [2,0,-1],
            [1,3,4],
            [-1,-1,3]])
result=np.dot(A,B)
print("A={}".format(A))
print("B={}".format(B))
print("AB={}".format(result))