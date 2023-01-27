def add(a1, b1):  # 相加函数
    c1 = a1 + b1
    return c1


def bubble_sort(array):  # 冒泡排序
    length = len(array)
    for i in range(length-1):
        for j in range(length - i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


a = 10
b = 20
c = add(a, b)
print(c)
arr = [13, 32, 25, 14, 76, 43]
bubble_sort(arr)
print(arr)
