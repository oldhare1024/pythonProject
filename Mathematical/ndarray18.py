import numpy as np

a = np.arange(6)
print('我们的数组是：')
print(a)
print('调用 id() 函数：')
print(id(a))
print('a 赋值给 b：')
b = a
print(b)
print('b 拥有相同 id()：')
print(id(b))
print('修改 b 的形状：')
b.shape = (3, 2)
print(b, id(b), sep='\n')
print('a 的形状也修改了：')
print(a, id(a), sep='\n')

c = np.arange(6).reshape(3, 2)
print('矩阵c为\n', c)
d = c.view()
print('矩阵d为\n', d)
print('c:', id(c), ', d:', id(d))
d.shape = (2,3 )
print(c, d,sep='\n')

arr = np.arange(12)
print ('我们的数组：')
print (arr)
print ('创建切片：')
e=arr[3:]
f=arr[3:]
e[1]=123
f[2]=234
print(arr)
print(id(e),id(f),id(arr[3:]))

a = np.array([[10,10],  [2,3],  [4,5]])
print ('数组 a：')
print (a)
print ('创建 a 的深层副本：')
b = a.copy()
print ('数组 b：')
print (b)
# b 与 a 不共享任何内容
print ('我们能够写入 b 来写入 a 吗？')
print (b is a)
print ('修改 b 的内容：')
b[0,0]  =  100
print ('修改后的数组 b：')
print (b)
print ('a 保持不变：')
print (a)