import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
print('矩阵a行与列的最小值各为{},{}\n'.format(np.amin(a, axis=0), np.amin(a, axis=1)))
print('矩阵a行与列的最大值各为{},{}\n'.format(np.amax(a, axis=0), np.amax(a, axis=1)))
print('矩阵a最大最小值相差为{}\n'.format(np.ptp(a)))

print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1, keepdims=True))

print(np.median(a))
print(np.mean(a))
wt = [1, 2, 3, 4]
a = [75, 60, 85, 100]
print(np.average(a, weights=wt))
print(np.std([1, 2, 3, 4]))
print(np.var([1, 2, 3, 4]))
