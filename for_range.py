All = 8
T = 0
while True:
    if All == 1:
        T += 1
        break
    elif All % 2 == 1:
        All //= 2
        T += 1
    else:
        All /= 2
print(int(T))
# while All != 1:
#     if All % 2 == 1:
#         All //= 2
#         T += 1
#     else:
#         All /= 2
# print(int(T + 1))
