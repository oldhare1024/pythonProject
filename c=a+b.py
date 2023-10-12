class Solution:
    def two_sum(self, n, targe):
        hashtable = dict()  # 创建哈希表
        for i, num in enumerate(n):  # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
            if targe - num in hashtable:
                print(hashtable[targe - num])
            hashtable[n[i]] = i  # 把列表的元素添加哈希表中
        return []


# arr = [1, 3, 5, 7, 8, 23, 13]
# a = int(input())
# print(two_sum(arr, a))
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[i] + arr[j] == a:
#             print(arr[i], arr[j])
#             break
s = Solution()
num = [2, 5, 7, 13]
com = s.two_sum(num, 12)
print(com)
