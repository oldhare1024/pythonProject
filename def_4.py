def count_sort(arr):
    maxi = max(arr)
    mini = min(arr)
    bucketlen = (maxi - mini) + 1  # 桶长度
    bucket = [0] * bucketlen  # 初始化创建长度为bucklen的列表
    sortedi = 0
    for i in range(len(arr)):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketlen):
        while bucket[j] > 0:
            arr[sortedi] = j
            sortedi += 1
            bucket[j] -= 1
    return arr


num = []
for k in range(5):
    num.append(int(input()))
count_sort(num)
print(num)
