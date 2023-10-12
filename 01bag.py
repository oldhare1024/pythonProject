m = int(input())
n = int(input())
w = [0 for i in range(n + 1)]
v = [0 for j in range(n + 1)]
dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    w[i] = int(input())
    v[i] = int(input())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= w[i] and dp[i - 1][j] < dp[i - 1][j - w[i]] + v[i]:
            dp[i][j] = dp[i - 1][j - w[i]] + v[i]
        else:
            dp[i][j] = dp[i - 1][j]
for i in range(n + 1):
    for j in range(m + 1):
        print(dp[i][j], end=' ')
    print("\n")
print(dp[n][m])
