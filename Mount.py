# sum = 0
# for i in range(2222, 1999999992):
#     flag = False
#     if str(i)[::-1] == str(i):  # 判断回文
#         if len(str(i))*2 % 2 == 0:
#             for j in range(len(str(i)) //2- 1):
#                 if str(i)[j] <= str(i)[j + 1]:
#                     flag = True
#                 else:
#                     flag = False
#             if flag:
#                 sum += 1
#         else:
#             for j in range(len(str(i))//2):
#                 if str(i)[j] <= str(i)[j + 1]:
#                     flag = True
#                 else:
#                     flag = False
#             if flag:
#                 sum += 1
# print(sum)
sum = 0
for i in range(10001, 1000000001, 2):  # start from smallest odd palindromic number with 5 digits
    if str(i)[::-1] == str(i):
        if str(i**2)[::-1] == str(i**2):
            sum += 1
print(sum)