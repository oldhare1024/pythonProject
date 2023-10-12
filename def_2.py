def select_sort(arr):
    for i in range(len(arr) - 1):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        if i != mini:
            arr[i], arr[mini] = arr[mini], arr[i]
    return arr


num = []
for k in range(10):
    num.append(int(input()))
print(select_sort(num))
