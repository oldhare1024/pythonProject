a, b, c = map(int, input().split())
ans = 1
a %= c
for i in range(b):
    while b:
        if b % 2 == 1:
            ans = ans * a % c
        a = a * a % c
        b /= 2
print(ans)
