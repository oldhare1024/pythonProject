s = [[0 for i in range(1010)] for i in range(1010)]
n, m, q = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = int(input())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
while q:
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1], end='\n')
