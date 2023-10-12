import math


def main(num):
    return math.factorial(num)


N = int(input())
sum = 0
for i in range(1, N + 1):
    sum += main(i)
print(sum)
