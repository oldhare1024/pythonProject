# 题解一
S, n = input().split()
n = int(n)
h, m, s = map(int, S.split(':'))
h += n // 3600
m += n % 3600 // 60
s += n % 60
if s >= 60:
    s = s % 60
    m += 1
if m >= 60:
    m = m % 60
    h += 1
if h >= 24:
    h = h % 24
print("%02d:" % h + "%02d:" % m + "%02d" % s)
# if h < 10 and m >= 10 and s >= 10:
#     print(f'0{h}:{m}:{s}')
# elif m < 10 and h >= 10 and s >= 10:
#     print(f'{h}:0{m}:{s}')
# elif s < 10 and m >= 10 and h >= 10:
#     print(f'{h}:{m}:0{s}')
# elif h < 10 and m < 10 and s < 10:
#     print(f'0{h}:0{m}:0{s}')
# elif h < 10 and m < 10 and s >= 10:
#     print(f'0{h}:0{m}:{s}')
# elif h >= 10 and m < 10 and s < 10:
#     print(f'{h}:0{m}:0{s}')
# elif h < 10 and m >= 10 and s < 10:
#     print(f'0{h}:{m}:0{s}')
# elif h >= 10 and m >= 10 and s >= 10:
#     print(f'{h}:{m}:{s}')


# 题解二
# import datetime
#
# S, n = input().split()
# n = int(n)
# now = S
# start_time1 = datetime.datetime.strptime(now, "%H:%M:%S")
# # 计算经过N秒后的时间
# new_time = start_time1 + datetime.timedelta(seconds=n)
#
# # 格式化输出时间
# print(new_time.strftime("%H:%M:%S"))
