import random
import time as t


def QuickSort(arr, l, r):
    if l >= r:
        return
    mid = arr[l]
    low = l
    high = r
    while low < high:
        while low < high and arr[high] >= mid:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < mid:
            low += 1
        arr[high] = arr[low]
        arr[low] = mid
        QuickSort(arr, l, low - 1)
        QuickSort(arr, low + 1, r)


def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    return result


def randomarr(n):
    num = []
    for i in range(0, n):
        number = random.randint(0, 100)
        num.append(number)
    return num


# arr=list(map(int,input().split()))
print('请输入3个随机数组的长度')

n1 = int(input())
n2 = int(input())
n3 = int(input())

arr1 = randomarr(n1)
arr2 = randomarr(n2)
arr3 = randomarr(n3)

start = t.perf_counter()

print(MergeSort(arr1))
end = t.perf_counter()
runtime = (end - start) * 1000
print('归并排序第一数组运行时间:', runtime)

start = t.perf_counter()
print(MergeSort(arr2))
end = t.perf_counter()
runtime = (end - start) * 1000
print('归并排序第二数组运行时间:', runtime)

start = t.perf_counter()
print(MergeSort(arr3))
end = t.perf_counter()
runtime = (end - start) * 1000
print('归并排序第三数组运行时间:', runtime)

start = t.perf_counter()
QuickSort(arr1, 0, len(arr1) - 1)
print(arr1)
end = t.perf_counter()
runtime = (end - start) * 1000
print('快速排序第一数组运行时间:', runtime)

start = t.perf_counter()
QuickSort(arr2, 0, len(arr2) - 1)
print(arr2)
end = t.perf_counter()
runtime = (end - start) * 1000
print('快速排序第二数组运行时间:', runtime)

start = t.perf_counter()
QuickSort(arr3, 0, len(arr3) - 1)
print(arr3)
end = t.perf_counter()
runtime = (end - start) * 1000
print('快速排序第三数组运行时间:', runtime)
