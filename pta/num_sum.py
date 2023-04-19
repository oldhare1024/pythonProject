A, B = map(int, input().split())
flag = 0
num = [i for i in range(A, B + 1)]
for i in range(len(num)):
    print("%5d" % num[i], end='')
    # print(num[i], end=' ')
    flag += 1
    if flag == 5:
        print('')
        flag = 0
print('')
print('Sum = ' + str(sum(num)))
