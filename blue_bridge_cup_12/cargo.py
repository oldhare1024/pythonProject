n = 2021041820210418
s = 0
long = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        long.add(i)
        long.add(n // i)
for i in long:
    for j in long:
        for k in long:
            if n == i * j * k:
                s += 1
print(s)
