s = input()
sum = 0
a = 1
for i in s:
    sum %= (10 ** 9 + 7)
    a %= (10 ** 9 + 7)
    if i == '1':
        sum += a
        a += 1
print(sum)
