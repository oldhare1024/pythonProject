n=int(input())
prisum = 0
for x in range(2,n):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        prisum += x
print(f'1~{n}内所有素数的和为：{prisum}')
