import turtle as t

a = 5 / 2
print(a)
b = 5 // 2
print(b)
c = 5 % 2
print(c)
# 网速转换计算器
a = t.numinput("请输入网速：", 'MB/s')
b = t.numinput("请输入下载文件大小：", 'GB')
c = b * 1024 // a // 60
d = b * 1024 // a % 60
print(str(int(c)) + '分钟' + str(int(d)) + '秒')
