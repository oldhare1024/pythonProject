n = int(input())
a = input()
a = list(map(int, a.strip().split()))
b = [0] * n
sumn = 0
j = 0
for i in range(n - 1):
    if a[i + 1] - a[i] == 1:
        sumn += 1
    else:
        b[j] = sumn
        j += 1
        sumn = 0
b[j] = sumn
print(max(b) + 1)
