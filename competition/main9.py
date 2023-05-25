str = input()
list = str.split()
k = int(list[0])
list[0:1] = []
str1 = ' '.join(list)
print(str1[:k])
