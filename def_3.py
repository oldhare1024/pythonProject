def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = []
for k in range(5):
    arr.append(int(input()))
insert_sort(arr)
print(arr)
