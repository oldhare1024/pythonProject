def fibo():
    a1 = i = 0
    a2 = 1
    while i <= 20:  # 生成前二十位斐波那契数列
        yield a1
        a1, a2 = a2, a1 + a2
        i += 1


for j in fibo():
    print(j)
