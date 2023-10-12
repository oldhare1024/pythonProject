import time

a = "ABBCBA"
b = "BCBA"

start = time.time()
# 方法1
for i in range(10000):
    if b in a:
        print(True)
# 方法2
# for i in range(500):
#     c = a.find(b)
#     print(c)

end = time.time()
print(end - start)
# 第一个方法循环300次耗时0.001004934310913086
# 第一个方法循环1000次耗时0.0051727294921875

# 第二个方法循环300次耗时0.0010077953338623047
# 第二个方法循环1000次耗时0.0030069351196289062
