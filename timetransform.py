import time as t

a = 24 * 60 * 60 * 1000  # 每一天的毫秒数
b = int(input())
start = t.time()
c = b % a
HH = int(c / 3600000)
MM = int(c % 3600000 / 60000)
SS = int(c % 60000 / 1000)
print(str("%02d" % HH) + ':' + str("%02d" % MM) + ':' + str("%02d" % SS))
end = t.time()
long = start - end
print("%.2f" % long)
