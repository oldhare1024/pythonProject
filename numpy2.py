import numpy as ny

a = ny.zeros((3, 2))
b = a.astype(int)
print(a, b, sep='\n\n')
c = ny.array((3, 2))
d = ny.array((4, 6))
print(c + d, c - d, c * d, sep=',')
