import numpy as np

s=b'Hello,World'
list=range(5)
it=iter(list)
x = [1, 2, 3]
y = (1, 2, 3)
z = [(1, 2, 3), (4, 5, 6)]
a = np.asarray(x)
b = np.asarray(y)
c = np.asarray(z,dtype=float)
d=np.frombuffer(s,dtype='S1')
e=np.fromiter(it,dtype=float)

print(a, b, c, d, e,sep='\n')
