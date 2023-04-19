import math
import timeit

start1 = timeit.default_timer()
n = int(input())

print(math.sqrt(n))

end1 = timeit.default_timer()
print("Running time = ", "%.2f" % (end1 - start1))
