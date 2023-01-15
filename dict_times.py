dt = {}
t = 1
# for t in input('请输入文字：'):
#     dt[t] = dt.get(t, 0) + 1
for t in input('请输入文字：'):
    if t in dt:
        dt[t] = dt[t] + 1
    else:
        dt[t] = 1
for k in dt:
    print(f'|{k}|出现了{dt[k]}次')
