S, n = input().split()
n = int(n)
h, m, s = map(int, S.split(':'))
hour = n // 3600
minute = n % 3600 // 60
second = n % 60
h += hour
m += minute
s += second
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
