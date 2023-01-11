import turtle as t

month = t.numinput('季节判断', '请输入月份')
if 3 <= month <= 5:
    print('春季')
elif 6 <= month <= 8:
    print('夏季')
elif 9 <= month <= 11:
    print('秋季')
elif month == 12 or 1 or 2:
    print('冬季')
else:
    print('输入错误')
