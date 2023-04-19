N = input()
digital = [0] * 10
i = j = k = 0
for i in N:
    digital[int(i)] += 1
for j in digital:
    if j != 0:
        print(f'{k}:{j}')
    k += 1
