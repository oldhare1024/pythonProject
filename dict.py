d = {
    'da': '打、答、达、哒、搭',
    'xiong': '熊，雄，胸、凶、芎',
    'mei': '妹、每、美、梅、枚'
}
i = j = 0
print(bool('da' in d))
for i in d.values():  # 返回字典中所有值
    print(i)
for i, j in d.items():  # 返回字典中所有键值对
    print(i, j)
for i in d.keys():  # 返回字典中所有键
    print(i)
di = {i: i ** 3 for i in range(5)}
print(di)
