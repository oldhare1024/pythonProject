N = int(input())
ID = []
s = 0
flag = 0
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
checkcodes = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
for i in range(N):
    ID.append(input())
    s = 0
    a = ID[i]
    if 'X' in a[:17]:
        print(a)
    else:
        for j in range(17):
            s += int(int(a[j]) * weights[j])
        z = s % 11
        if str(checkcodes[z]) != a[17]:
            print(a)
            flag = 0
        else:
            flag += 1
if flag == N:
    print("All passed")
