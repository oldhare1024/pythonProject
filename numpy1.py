import numpy

a = numpy.power(10, 5)
j = 0
print(a)
for i in range(10):
    j += i
else:
    j *= 10
for n in range(2, 50):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
