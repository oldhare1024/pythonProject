s = input()
t = input()
yis = ers = 0
yit = ert = 0
if t in s:
    print("Yes")
else:
    for i in s:
        if i == '1':
            yis += 1
        else:
            ers += 1
    for i in t:
        if i == '1':
            yit += 1
        else:
            ert += 1
    if yis >= yit and ers >= ert:
        print("Yes")
    else:
        print("No")
