n, m = map(int, input().split())
catfrd = list(map(int, input().split()))
catexpfrd = list(map(int, input().split()))
peofrd = list(map(int, input().split()))
peoexpfrd = list(map(int, input().split()))
flag = 0
i = j = 0
s = str()
max1 = min(peofrd)
for i in range(n):
    flag = 0
    for j in range(m):
        if catfrd[i] >= peoexpfrd[j] and catexpfrd[i] <= peofrd[j]:
            flag = 1
            max1 = max(max1, peofrd[j])
        else:
            continue
    if flag == 0:
        # print(int(-1), end=' ')
        s = s + '-1 '
    else:
        # print(max1, end=' ')
        s = s + str(max1) + ' '
        #peofrd[j] = 0
number = list(map(int, s.split()))
print(" ".join(str(i) for i in number))
