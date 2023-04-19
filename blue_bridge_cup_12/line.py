# 截距：d = - k * x1 + y1 = (x2 * y1 - x1 * y2) / (x2 - x1)
# (y1-y2)/(x2-x1)*x1+y1=(y1*x1-y2*x1)/(x2-x1)+y1=[(y1*x1-y2*x1)+y1*(x2-x1)]/(x2-x1)=[y1*x1-y2*x1+y1*x2-y1*x1]/(x2-x1)=[y1*x2-y2*x1]/(x2-x1)
point = [[i, j] for i in range(20) for j in range(21)]
line = set()
for i in range(len(point) - 1):
    x1, y1 = point[i][0], point[i][1]
    for j in range(i, len(point)):
        x2, y2 = point[j][0], point[j][1]
        if x1 - x2 == 0:
            continue
        else:
            k = (y2 - y1) / (x2 - x1)
            # d = -1*k * x1 + y1
            d = (x2 * y1 - x1 * y2) / (x2 - x1)
        if (k, d) not in line:
            line.add((k, d))
print(len(line) + 20)
