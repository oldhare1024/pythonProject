import numpy as np

a = np.array([1, 2, 3, 4, 5])
np.save('outfile_numpy.npy', a)
b=np.load('outfile_numpy.npy')
print(b)
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sin_array
np.savez("runoob.npz", a, b, sin_array = c)
r = np.load("runoob.npz")
print(r.files) # 查看各个数组名称
print(r["arr_0"]) # 数组 a
print(r["arr_1"]) # 数组 b
print(r["sin_array"]) # 数组 c

a = np.array([1, 2, 3, 4, 5])
np.savetxt('out.txt', a)
b = np.loadtxt('out.txt')

print(b)

a = np.arange(0, 10, 0.5).reshape(4, -1)
np.savetxt("out1.txt", a, fmt="%d", delimiter=",")  # 改为保存为整数，以逗号分隔
b = np.loadtxt("out1.txt", delimiter=",")  # load 时也要指定为逗号分隔
print(b)