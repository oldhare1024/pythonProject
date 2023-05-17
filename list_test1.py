import random

# 生成一个【0，10】长度为100的随机序列
random_int_list = [2, 1]
alltime = 0
while random_int_list != sorted(random_int_list):
    random_int_list.clear()
    random_int_list=random.sample(range(1, 10),5)
    alltime += 1
    if alltime > 100000:
        break
print(random_int_list)
print(alltime)
