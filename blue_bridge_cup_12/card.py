card = [2021 for i in range(10)]
# c=[i for i in range(10)]
for i in range(20210):
    flag = False
    for j in range(len(str(i))):
        card[int(str(i)[j])] -= 1
        if card[int(str(i)[j])] <= 0:
            print(i)
            flag = True
            break
    if flag == True:
        break
