N = int(input())
L = 1
start = 0
f = []
f2 = []
i = j = k = 0


def isprime(N):  # 判断素数
    for i in range(2, int(N ** 0.5 + 1)):
        if N % i == 0:
            return 0  # 返回0不为素数
    return 1  # 返回1为素数


if isprime(N):
    print("1", N, sep='\n')
else:
    for k in range(2, int(N ** 0.5 + 1)):
        if N % k == 0:
            f.append(k)
    for l in range(len(f)-1):
        if f[l + 1] - f[l] == 1:
            f2.append(f[l])
        elif f[l] - f[l-1]==1:
            f2.append(f[l])
        else:
            continue
    print(f2)
    for i in range(len(f2)):
        s = 1  # 乘积
        j = i
        while s * f2[j] <= N:
            s = s * f2[j]
            if N % s == 0 and f2[j] - f2[i] + 1 > L:
                start = f2[i]
                L = f2[j] - f2[i] + 1
            j += 1
            if j >= len(f2):
                break
    print(L)
    for i in range(start, start + L):
        if i == start:
            print(i, end='')
        else:
            print(f'*{i}', end='')
