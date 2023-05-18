n, m = map(int, input().split())
jimu = list(map(int, input().split()))
for i in range(m):
    q = input()
    if q == '2':
        set1 = set(jimu)  # 集合具有自动去重功能
        print(len(set1), end='\n')
    else:
        com, x, y = map(int, q.split())
        z = jimu[x - 1] // 2
        jimu[y - 1] += jimu[x - 1] // 2
        if jimu[x - 1] & 1 == 1:
            jimu[x - 1] -= z
