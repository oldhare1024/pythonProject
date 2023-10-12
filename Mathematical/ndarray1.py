import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
c = np.array([1, 2, 3, 4, 5], ndmin=2)
d = np.array([1, 2, 3], dtype=complex)

e = np.dtype(np.int32)
f = np.dtype('i8')
g = np.dtype('<i4')

h = np.dtype([('age', np.int8)])
i = np.array([(10,), (20,), (30,)], dtype=h)
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
j = np.array([('abc', 21, 60), ('xyz', 18, 75)], dtype=student)

print(a, b, c, d, sep='\n')
print(e, f, g, sep='\n')
print(h, i, sep='\n')
print(i['age'])
print(j)
