c = []
i = 0
a = 1
print(f"请输入汽车品牌：")
while a != '0':
    a = input()
    c.insert(i, a)
    i += 1
del c[len(c)-1]
print(f"一共{len(set(c))}种汽车品牌：")
print(set(c))
