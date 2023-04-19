def young(N):
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            s = k = 1
            # 计算第 i 行的第 j 个数
            for k in range(1, j):
                s = int(s * (i - k) / k)
                if s == N:
                    return int((i - 1) * i / 2 + j)


N = int(input())
if N <= 4:
    print(1)
else:
    print(young(N))

