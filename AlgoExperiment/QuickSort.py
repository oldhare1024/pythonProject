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


arr = list(map(int, input().split()))
QuickSort(arr, 0, len(arr) - 1)
print(arr)
