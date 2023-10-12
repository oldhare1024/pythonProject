import numpy as np

a = np.arange(8)
print('原始数组:{}\n'.format(a))
b = a.reshape(4, 2)
print('修改后的数组:\n{}\n'.format(b))
c = np.arange(9).reshape(3, 3)
print('原始数组:')
for row in c:
    print(row)
print('迭代后的数组:')
for elem in c.flat:
    print(elem)
print(a.flatten())
print(a.reshape(4, 2).flatten(order='F'))
print(c.ravel(), end='\n')
d = np.arange(12).reshape(3, 4)
print(d, end='\n\n')
print(np.transpose(d))
if np.transpose(d).all() == d.T.all():
    print('yes')
else:
    print('no')
e = np.arange(8).reshape((2, 2, 2))
#np.reshape(e, 2, 2, 2)
print(e,end='\n')
f=np.rollaxis(e,2,0)
print(f,end='\n')

g = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(g)
print('\n')
h = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(h)
print('\n')
# 两个数组的维度相同

print('沿轴 0 连接两个数组：')
print(np.concatenate((g, h)))
print('\n')

print('沿轴 1 连接两个数组：')
print(np.concatenate((g, h), axis=1))