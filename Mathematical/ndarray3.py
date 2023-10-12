import numpy as np

a = np.empty([3, 2], dtype=int)
b = np.zeros((2, 4), dtype=int, order='C')
c = np.ones((2, 4), dtype=[('x', 'i4'), ('y', 'float')])
d = np.zeros_like(c, dtype=None, order='K', subok=True, shape=None)

print(a, b, c, d, sep='\n')
