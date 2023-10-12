def MaxSubArr(arr, l, r):  # 求最大子数组和函数
    if l == r:  # 如果左右指针位置相同，则只有一个元素
        if arr[l] > 0:  # 该元素为正数则添加到数组中
            return arr[l]
        else:  # 否则不添加该元素
            return 0
    m = (l + r) // 2  # 求出中间下标
    maxleftsum = MaxSubArr(arr, l, m)  # 递归求出最大左子数组和
    maxrightsum = MaxSubArr(arr, m + 1, r)  # 递归求出最大右子数组和

    leftbordersum = maxleftbordersum = 0  # 前缀和算法求左子数组最大值范围为[0,mid]
    for i in range(m, l - 1, -1):  # 从中间位置向左开始求前缀和
        leftbordersum += arr[i]  # 前缀和算法
        if leftbordersum > maxleftbordersum:  # 求最大的前缀和
            maxleftbordersum = leftbordersum

    maxrightbordersum = rightbordersum = 0  # 前缀和算法求右子数组最大值范围为[mid+1,right]
    for j in range(m + 1, r + 1):  # 从中间位置向右开始求前缀和
        rightbordersum += arr[j]  # 前缀和算法
        if rightbordersum > maxrightbordersum:  # 求最大的前缀和
            maxrightbordersum = rightbordersum
    return max(maxleftsum, maxrightsum, maxleftbordersum + maxrightbordersum)
    # 返回值为左子数组的最大子数组，右子数组的最大子数组和左子数组开始位置到右子数组结束位置包括中间元素的数组，这三者中最大值


arr = list(map(int, input().split()))  # map配合split将字符串转换为int类型列表
print(MaxSubArr(arr, 0, len(arr) - 1))  # 输出结果
