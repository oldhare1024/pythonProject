def div(m, n):  # 辗转相除法求最大公约数
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


# def div(m, n):  # 递归求最大公约数
#     if n == 0:
#         return m
#     return div(n, m % n)


a = int(input())
b = int(input())
print(div(a, b))
