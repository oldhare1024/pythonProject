def binarysearch(num1, target):
    left = 0
    right = len(num1) - 1
    # 在list[left...right]里查找target，注意是左闭右闭
    while left <= right:
        mid = (right + left) // 2  # 取中间元素索引
        if num1[mid] == target:
            return mid
        elif target > num1[mid]:
            left = mid + 1  # 到list[mid + 1 ...right]里查找
        else:  # target < list[mid]
            right = mid - 1  # 到list[left ...mid - 1]里查找
    return -1  # 未找到target元素


tar = int(input())
num = []
for i in range(6):
    num.append(int(input()))
print(binarysearch(sorted(num), tar))
