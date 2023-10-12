import numpy as np

a = np.array([[3, 7], [9, 1]])

print('排序前为\n{}'.format(a))
print('排序后为\n{}'.format(np.sort(a)))
print('排序后为\n{}'.format(np.sort(a, kind='mergesort')))
print('排序后为\n{}'.format(np.sort(a, kind='heapsort')))
print('按列排序为\n{}'.format(np.sort(a, axis=0)))

b = np.dtype([('name', 'S10'), ('age', int)])
a1 = np.array([("daju", 21), ("anil", 25), ("bavi", 17), ("cmar", 27)], dtype=b)

print('数组排序前为\n{}'.format(a))
print('数组按name字段排序为\n{}'.format(np.sort(a1, order='name')))
print('数组按age字段排序为\n{}'.format(np.sort(a1, order='age')))

x = np.array([3, 1, 2])
y = np.argsort(x)

print(x, y, x[y], sep='\n')

for i in y:
    print(x[i], end=' ')

name = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.v', 's.v', 's.y', 'f.y')
ind = np.lexsort((dv, name))

print()
print(ind)
print([name[i] + "," + dv[i] for i in ind])

c = np.sort_complex([5 + 2j, 1 + 0j, 2 + 8j, 2 + 0.5j, 1 + 7j])

print(c)

d = np.array([3, 4, 2, 1])
e = np.partition(d, 3)

print(e, end='\n')

f = np.array([46, 42, 425, 46, 24, 84, 10, 23])

print(f[np.argpartition(f, 2)[2]])
print(f[np.argpartition(f, -2)[-2]])

import numpy as np

a2 = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(a2)
print('调用 argmax() 函数：')
print(np.argmax(a2))
print('展开数组：')
print(a2.flatten())
print('沿轴 0 的最大值索引：')
maxindex = np.argmax(a2, axis=0)
print(maxindex)
print('沿轴 1 的最大值索引：')
maxindex = np.argmax(a2, axis=1)
print(maxindex)
print('调用 argmin() 函数：')
minindex = np.argmin(a2)
print(minindex)
print('展开数组中的最小值：')
print(a2.flatten()[minindex])
print('沿轴 0 的最小值索引：')
minindex = np.argmin(a2, axis=0)
print(minindex)
print('沿轴 1 的最小值索引：')
minindex = np.argmin(a2, axis=1)
print(minindex, end='\n')

a3 = np.array([[30, 20, 0], [24, 0, 2]])
print('{}中非零元素的索引为{}'.format(a3, np.nonzero(a3)))

x1 = np.arange(9.).reshape(3, 3)
print('数组\n{}\n中大于3的元素索引为{},值为{}'.format(x1, np.where(x1 > 3), x1[np.where(x1 > 3)]))

x2=np.arange(9.).reshape(3,3)

condition=np.mod(x2,2)==0
print(condition)
print('数组\n{}\n中满足条件的是{}'.format(x2,np.extract(condition,x2)))
