import timeit

n = int(input())
start1 = timeit.default_timer()

n=n**0.5
print(n)

end1 = timeit.default_timer()
print("Running time = ", "%.2f" % (end1 - start1))
