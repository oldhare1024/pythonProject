n, m = map(int, input().split())
bao = []
bao = input().split()
All = [0] * n
for i in range(len(bao)):
    bao[i] = int(bao[i])
# n个堡垒，列表存储能量值
for i in range(m):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        if All[j] == 1:
            continue
        else:
            if bao[j] - 100 <= 0:
                All[j] = 1
                continue
            else:
                bao[j] -= (bao[j] // 10 + 100)
            if bao[j] <= 0:
                All[j] = 1

print(sum(All))
