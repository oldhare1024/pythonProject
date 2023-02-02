def div(m, n):  # 递归求最大公约数
    if n == 0:
        return m
    return div(n, m % n)


a = int(input())
b = int(input())
if b > a:
    a, b = b, a
else:
    pass

mult = a * b + div(a, b)
print(mult)
