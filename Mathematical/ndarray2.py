import numpy as np

a = np.arange(24)
b = a.reshape(6, 4)
c = np.array([[1, 2, 3], [4, 5, 6]])
c.shape = (3, 2)
d = c.reshape(1, 6)
e = np.array([1, 2, 3, 4, 5], dtype=np.int8)
f = np.array([1, 2, 3, 4, 5], dtype=np.float64)

print(a.ndim, b.ndim, sep=' ')
print(c, d, sep='\n')
print(e.itemsize,f.itemsize,sep=' ')
print(a.flags)
