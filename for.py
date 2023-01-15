# import turtle as t
# t.speed(10)
# for i in range(80):
#     t.forward(i*4)
#     t.right(90)
# i = 1
# for i in range(i, 5):
#     print(i)
lst1 = [1, 3, 5, 7, 8]
lst2 = [2, 2, 7, 9, 7]
sum_number = 0
for i in lst1:
    for j in lst2:
        if i + j == 10:
            sum_number += j
print(sum_number)
# t.mainloop()
