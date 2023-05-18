n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))  # 存储各堡垒能量
# 从1开始
for i in range(m):
    l, r = map(int, input().split())
    a[l:r+1] = [x - (x // 10 + 100) for x in a[l:r+1]]
ans = 0
for i in range(1, n + 1):
    if a[i] <= 0:
        ans += 1
print(ans)  