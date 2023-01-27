# Len = 0
# for i in range(1, 2021):
#     if i < 10:
#         Len += 1
#     elif 10 <= i < 100:
#         Len += 2
#     elif 100 <= i < 1000:
#         Len += 3
#     elif 1000 <= i < 2021:
#         Len += 4
# print(Len)

Len = '1'
for i in range(2, 2021):
    Len += str(i)
print(len(Len))
