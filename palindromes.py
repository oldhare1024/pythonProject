# 请在此输入您的代码
def calc(value):
    result = []
    while value:
        result.append(value % 10)
        value = value // 10
    # 逆序，按正常的顺序返回
    result.reverse()
    return result


# 20200202
# 01234567
def judge3(nl):
    if nl[4] == 0:
        if nl[5] == 1 or nl[5] == 3 or nl[5] == 5 or nl[5] == 7 or nl[5] == 8:
            if 0 <= nl[6] <= 3:
                if nl[6] == 3 and 0 <= nl[7] <= 1:
                    return 1
                else:
                    return 0

    elif nl[4] == 1:
        if nl[5] == 1 and 0 <= nl[6] <= 3:
            if nl[6] == 3 and nl[7] == 0:
                return 1
            elif 0 <= nl[6] <= 2:
                return 1
            else:
                return 0
        elif nl[5] == 2 and 0 <= nl[6] <= 3:
            if nl[6] == 3 and 0 <= nl[7] < 2:
                return 1
    else:
        return 0


def judge1(nl):
    flag = False
    for i in range(0, 4):
        if nl[i] == nl[7 - i]:
            flag = True
        else:
            flag = False
            break
    return flag


def judge2(nl):
    if nl[0] == nl[2] == nl[5] == nl[7] and nl[1] == nl[3] == nl[4] == nl[6]:
        flag = True
    else:
        flag = False
    return flag


n = int(input())
j = 0
for j in range(n + 1, 89991232):
    if judge1(calc(j)) and judge3(calc(j)):
        print(j)
        break
for k in range(j, 89991232):
    if judge2(calc(k)) and judge3(calc(k)):
        print(k)
        break
