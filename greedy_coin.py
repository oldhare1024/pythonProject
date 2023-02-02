sta = input().rstrip()
end = input().rstrip()
sta_nums = []
end_nums = []
ant = 0
for i in sta:
    if i == '*':
        sta_nums.append(1)
    else:
        sta_nums.append(0)
for j in end:
    if j == '*':
        sta_nums.append(1)
    else:
        sta_nums.append(0)
for i in range(len(sta_nums) - 1):
    if end_nums[i] != sta_nums[i]:
        sta_nums[i], sta_nums[i + 1] = int(not sta_nums[i]), int(not sta_nums[i + 1])
        ant += 1
    print(ant)

